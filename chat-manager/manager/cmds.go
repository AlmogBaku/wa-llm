package manager

import (
	"chat-manager/proto"
	"context"
	"fmt"
	waProto "go.mau.fi/whatsmeow/binary/proto"
	"go.mau.fi/whatsmeow/types"
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
	default:
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
