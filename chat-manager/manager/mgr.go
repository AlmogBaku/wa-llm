package manager

import (
	"chat-manager/proto"
	"context"
	"fmt"
	"github.com/google/uuid"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/appstate"
	waProto "go.mau.fi/whatsmeow/binary/proto"
	"go.mau.fi/whatsmeow/types"
	"go.mau.fi/whatsmeow/types/events"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/protobuf/types/known/timestamppb"
	"os"
	"time"
	"unsafe"
)

type ChatManager interface {
	EventHandler(e any)
	proto.ChatManagerServer
}

type mgr struct {
	events chan *proto.Event
	client *whatsmeow.Client
	logger waLog.Logger
}

func New(client *whatsmeow.Client, log waLog.Logger) ChatManager {
	return &mgr{client: client, logger: log, events: make(chan *proto.Event, 100)}
}

func (m *mgr) Subscribe(sr *proto.SubscribeRequest, stream proto.ChatManager_SubscribeServer) error {
	m.logger.Infof("New client subscribed %s", sr.GetUuid())
	for {
		select {
		case e := <-m.events:
			e.SubscriptionId = sr.Uuid
			err := stream.Send(e)
			if err != nil {
				m.logger.Errorf("failed to send event: %v", err)
			}
		case <-stream.Context().Done():
			return nil
		}
	}

}

func (m *mgr) EventHandler(e any) {
	switch evnt := e.(type) {
	case *events.AppStateSyncComplete:
		if len(m.client.Store.PushName) > 0 && evnt.Name == appstate.WAPatchCriticalBlock {
			err := m.client.SendPresence(types.PresenceAvailable)
			if err != nil {
				m.logger.Warnf("Failed to send available presence: %v", err)
			} else {
				m.logger.Infof("Marked self as available")
			}
		}
	case *events.Connected, *events.PushNameSetting:
		if len(m.client.Store.PushName) == 0 {
			return
		}
		// Send presence available when connecting and when the pushname is changed.
		// This makes sure that outgoing messages always have the right pushname.
		err := m.client.SendPresence(types.PresenceAvailable)
		if err != nil {
			m.logger.Warnf("Failed to send available presence: %v", err)
		} else {
			m.logger.Infof("Marked self as available")
		}
	case *events.StreamReplaced:
		os.Exit(0)
	case *events.KeepAliveTimeout:
		m.logger.Debugf("Keepalive timeout event: %+v", evnt)
		if evnt.ErrorCount > 3 {
			m.logger.Debugf("Got >3 keepalive timeouts, forcing reconnect")
			go func() {
				m.client.Disconnect()
				err := m.client.Connect()
				if err != nil {
					m.logger.Errorf("Error force-reconnecting after keepalive timeouts: %v", err)
				}
			}()
		}
	case *events.KeepAliveRestored:
		m.logger.Debugf("Keepalive restored")
	case *events.Message:
		m.MessageHandler(evnt)
	}
}

func (m *mgr) MessageHandler(msg *events.Message) {
	if msg.Info.IsFromMe {
		return
	}

	m.dispatchRuntimeEvent(msg)
}

func (m *mgr) dispatchRuntimeEvent(e any) {
	pEvent := &proto.Event_MessageEvent{}
	switch ev := e.(type) {
	case *events.Message:
		pe := messageToEvent(ev)
		pEvent.MessageEvent = &pe
	default:
		m.logger.Warnf("Unsupported event: %v", e)
		return
	}

	m.events <- &proto.Event{
		Uuid:      uuid.NewString(),
		Timestamp: timestamppb.New(time.Now()),
		AccountContext: &proto.AccountContext{
			Id:             m.client.Store.ID.String(),
			RegistrationId: m.client.Store.RegistrationID,
			Platform:       m.client.Store.Platform,
			BusinessName:   m.client.Store.BusinessName,
			PushName:       m.client.Store.PushName,
		},
		Event: pEvent,
	}
}
func (m *mgr) Execute(ctx context.Context, cmd *proto.Command) (*proto.CommandResponse, error) {
	switch cmd.Operation.(type) {
	case *proto.Command_MessageCmd:
		return m.sendMessageCmd(ctx, cmd)
	case *proto.Command_AckCmd:
		return m.ackMessageCmd(ctx, cmd)
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

func messageToEvent(msg *events.Message) proto.MessageEvent {
	return proto.MessageEvent{
		Info: &proto.MessageInfo{
			MessageSource: &proto.MessageSource{
				Chat:               msg.Info.MessageSource.Chat.String(),
				Sender:             msg.Info.MessageSource.Sender.String(),
				IsFromMe:           msg.Info.MessageSource.IsFromMe,
				IsGroup:            msg.Info.MessageSource.IsGroup,
				BroadcastListOwner: msg.Info.MessageSource.BroadcastListOwner.String(),
			},
			Id:             msg.Info.ID,
			Type:           msg.Info.Type,
			PushName:       msg.Info.PushName,
			Timestamp:      timestamppb.New(msg.Info.Timestamp),
			Category:       msg.Info.Category,
			Multicast:      msg.Info.Multicast,
			MediaType:      msg.Info.MediaType,
			VerifiedName:   (*proto.VerifiedNameCertificate)(unsafe.Pointer(msg.Info.VerifiedName)),
			DeviceSentMeta: (*proto.DeviceSentMeta)(unsafe.Pointer(msg.Info.DeviceSentMeta)),
		},
		Message: (*proto.Message)(unsafe.Pointer(msg.Message)),
	}
}
