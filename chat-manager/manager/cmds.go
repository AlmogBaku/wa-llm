package manager

import (
	"chat-manager/proto"
	"context"
	"fmt"
	"go.mau.fi/whatsmeow"
	waProto "go.mau.fi/whatsmeow/binary/proto"
	"go.mau.fi/whatsmeow/types"
	"net/url"
	"os"
	"path"
	"unsafe"
)

func (m *mgr) Execute(ctx context.Context, cmd *proto.Command) (*proto.CommandResponse, error) {
	switch cmd.Operation.(type) {
	case *proto.Command_MessageCmd:
		return m.sendMessageCmd(ctx, cmd)
	case *proto.Command_AckCmd:
		return m.ackMessageCmd(ctx, cmd)
	case *proto.Command_GroupInfoCmd:
		return m.groupInfoCmd(ctx, cmd)
	case *proto.Command_DownloadCmd:
		return m.downloadMediaCmd(ctx, cmd)
	default:
		m.logger.Warnf("Unknown action: %v", cmd.Operation)
		return nil, fmt.Errorf("unknown action: %v", cmd.Operation)
	}
}

func (m *mgr) sendMessageCmd(ctx context.Context, cmd *proto.Command) (*proto.CommandResponse, error) {
	cm := cmd.GetMessageCmd()
	if cm.GetTo() == "" || cm.GetMessage() == nil {
		m.logger.Warnf("Invalid command: %v", cmd)
		return nil, fmt.Errorf("invalid command: %v", cmd)
	}

	to, err := types.ParseJID(cm.To)
	if err != nil {
		m.logger.Warnf("Failed to parse recipient: %v", err)
		return nil, fmt.Errorf("failed to parse recipient: %v", err)
	}

	msg := (*waProto.Message)(unsafe.Pointer(cm.GetMessage()))

	_, err = m.client.SendMessage(ctx, to, msg)
	if err != nil {
		m.logger.Warnf("Failed to send message: %v", err)
		return nil, fmt.Errorf("failed to send message: %v", err)
	}
	return &proto.CommandResponse{Uuid: cmd.Uuid}, nil
}

func (m *mgr) ackMessageCmd(ctx context.Context, cmd *proto.Command) (*proto.CommandResponse, error) {
	ack := cmd.GetAckCmd()

	chat, err := types.ParseJID(ack.GetChatJid())
	if err != nil {
		m.logger.Warnf("Failed to parse chat jid: %v", err)
		return nil, fmt.Errorf("failed to parse chat jid: %v", err)
	}

	sender, err := types.ParseJID(ack.GetSenderJid())
	if err != nil {
		m.logger.Warnf("Failed to parse sender jid: %v", err)
		return nil, fmt.Errorf("failed to parse sender jid: %v", err)
	}

	err = m.client.MarkRead(ack.MessageIds, ack.GetTimestamp().AsTime(), chat, sender)
	if err != nil {
		m.logger.Warnf("Failed to send ack: %v", err)
		return nil, fmt.Errorf("failed to send ack: %v", err)
	}
	return &proto.CommandResponse{Uuid: cmd.Uuid}, nil
}

func (m *mgr) downloadMediaCmd(ctx context.Context, cmd *proto.Command) (*proto.CommandResponse, error) {
	var downloadableMessage whatsmeow.DownloadableMessage
	switch v := cmd.GetDownloadCmd().DownloadableMessage.(type) {
	case *proto.DownloadCmd_AudioMessage:
		downloadableMessage = v.AudioMessage
	case *proto.DownloadCmd_DocumentMessage:
		downloadableMessage = v.DocumentMessage
	case *proto.DownloadCmd_ExternalBlobReference:
		downloadableMessage = v.ExternalBlobReference
	case *proto.DownloadCmd_HistorySyncNotification:
		downloadableMessage = v.HistorySyncNotification
	case *proto.DownloadCmd_ImageMessage:
		downloadableMessage = v.ImageMessage
	case *proto.DownloadCmd_PaymentBackgroundMediaData:
		downloadableMessage = v.PaymentBackgroundMediaData
	case *proto.DownloadCmd_StickerMessage:
		downloadableMessage = v.StickerMessage
	case *proto.DownloadCmd_StickerMetadata:
		downloadableMessage = v.StickerMetadata
	case *proto.DownloadCmd_VideoMessage:
		downloadableMessage = v.VideoMessage
	default:
		return nil, fmt.Errorf("unknown downloadable message: %v", v)
	}

	b, err := m.client.Download(downloadableMessage)
	if err != nil {
		m.logger.Errorf("Failed to download media: %w", err)
		return nil, fmt.Errorf("failed to download media: %v", err)
	}
	//save to file
	u, err := url.Parse(downloadableMessage.GetDirectPath())
	if err != nil {
		m.logger.Errorf("Failed to parse url: %w", err)
		return nil, fmt.Errorf("failed to parse url: %v", err)
	}

	dname, err := os.MkdirTemp("", "chat-manager")
	if err != nil {
		m.logger.Errorf("Failed to create temporary directory: %w", err)
		return nil, fmt.Errorf("failed to create temporary directory: %v", err)
	}

	fname := fmt.Sprintf("%s/%s-%s", dname, cmd.GetDownloadCmd().GetChatJid(), path.Base(u.Path))
	file, err := os.Create(fname)
	if err != nil {
		m.logger.Errorf("Failed to create file: %w", err)
		return nil, fmt.Errorf("failed to create file: %v", err)
	}

	defer file.Close()
	_, err = file.Write(b)
	if err != nil {
		m.logger.Errorf("Failed to write file: %w", err)
		return nil, fmt.Errorf("failed to write file: %v", err)
	}
	return &proto.CommandResponse{
		Uuid: cmd.Uuid,
		Response: &proto.CommandResponse_DownloadResponse{
			DownloadResponse: &proto.DownloadResponse{
				MessageId: cmd.GetDownloadCmd().MessageId,
				FileUri:   fmt.Sprintf("file://%s", file.Name()),
			},
		},
	}, nil
}
