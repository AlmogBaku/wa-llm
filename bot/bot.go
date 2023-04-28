package bot

import (
	"context"
	"github.com/google/uuid"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/appstate"
	waProto "go.mau.fi/whatsmeow/binary/proto"
	"go.mau.fi/whatsmeow/types"
	"go.mau.fi/whatsmeow/types/events"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/protobuf/types/known/timestamppb"
	"io"
	"os"
	"time"
	"unsafe"
	"wa-group-admin/proto"
)

type Bot interface {
	EventHandler(e any)
}

type bot struct {
	handlerRt proto.HandlerClient
	events    chan *proto.Event
	client    *whatsmeow.Client
	logger    waLog.Logger
}

func New(rt proto.HandlerClient, client *whatsmeow.Client, log waLog.Logger) Bot {
	b := &bot{handlerRt: rt, client: client, logger: log, events: make(chan *proto.Event, 100)}
	go b.runtimeHandlerLoop()
	return b
}

func (b *bot) runtimeHandlerLoop() {
	for {
		ctx, cancel := context.WithCancel(context.Background())

		stream, err := b.handlerRt.Handle(context.Background())
		if err != nil {
			b.logger.Errorf("failed to handle: %v", err)
			cancel()
			time.Sleep(5 * time.Second)
			continue
		}
		go func() {
			for {
				select {
				case <-ctx.Done():
					return
				default:

				}

				defer cancel()
				cmd, err := stream.Recv()
				if err != nil {
					if err == io.EOF {
						b.logger.Infof("stream closed. reconnecting...")
						return
					}
					b.logger.Errorf("failed to receive: %v", err)
					return
				}
				b.processCommand(ctx, cmd)
			}
		}()
		go func() {
			for {
				select {
				case <-ctx.Done():
					return
				case evnt := <-b.events:
					err := stream.Send(evnt)
					if err != nil {
						b.logger.Errorf("failed to send: %v", err)
						cancel()
						return
					}
				}
			}
		}()
	}
}

func (b *bot) EventHandler(e any) {
	switch evnt := e.(type) {
	case *events.AppStateSyncComplete:
		if len(b.client.Store.PushName) > 0 && evnt.Name == appstate.WAPatchCriticalBlock {
			err := b.client.SendPresence(types.PresenceAvailable)
			if err != nil {
				b.logger.Warnf("Failed to send available presence: %v", err)
			} else {
				b.logger.Infof("Marked self as available")
			}
		}
	case *events.Connected, *events.PushNameSetting:
		if len(b.client.Store.PushName) == 0 {
			return
		}
		// Send presence available when connecting and when the pushname is changed.
		// This makes sure that outgoing messages always have the right pushname.
		err := b.client.SendPresence(types.PresenceAvailable)
		if err != nil {
			b.logger.Warnf("Failed to send available presence: %v", err)
		} else {
			b.logger.Infof("Marked self as available")
		}
	case *events.StreamReplaced:
		os.Exit(0)
	case *events.KeepAliveTimeout:
		b.logger.Debugf("Keepalive timeout event: %+v", evnt)
		if evnt.ErrorCount > 3 {
			b.logger.Debugf("Got >3 keepalive timeouts, forcing reconnect")
			go func() {
				b.client.Disconnect()
				err := b.client.Connect()
				if err != nil {
					b.logger.Errorf("Error force-reconnecting after keepalive timeouts: %v", err)
				}
			}()
		}
	case *events.KeepAliveRestored:
		b.logger.Debugf("Keepalive restored")
	case *events.Message:
		b.MessageHandler(evnt)
	}
}

func (b *bot) MessageHandler(msg *events.Message) {
	if msg.Info.IsFromMe {
		return
	}

	b.dispatchRuntimeEvent(msg)
}

func (b *bot) dispatchRuntimeEvent(e any) {
	pEvent := &proto.Event_MessageEvent{}
	switch ev := e.(type) {
	case *events.Message:
		pe := messageToEvent(ev)
		pEvent.MessageEvent = &pe
	default:
		b.logger.Warnf("Unsupported event: %v", e)
		return
	}

	b.events <- &proto.Event{
		Uuid:      uuid.NewString(),
		Timestamp: timestamppb.New(time.Now()),
		AccountContext: &proto.AccountContext{
			Id:             b.client.Store.ID.String(),
			RegistrationId: b.client.Store.RegistrationID,
			Platform:       b.client.Store.Platform,
			BusinessName:   b.client.Store.BusinessName,
			PushName:       b.client.Store.PushName,
		},
		Event: pEvent,
	}
}
func (b *bot) processCommand(ctx context.Context, cmd *proto.Command) {
	switch cmd.Action {
	case proto.Command_NONE:
		return
	case proto.Command_SEND_MESSAGE:
		if cmd.Recipient == "" || cmd.Payload == nil {
			b.logger.Warnf("Invalid command: %v", cmd)
			return
		}

		recipient, err := types.ParseJID(cmd.Recipient)
		if err != nil {
			b.logger.Warnf("Failed to parse recipient: %v", err)
			return
		}

		payload, err := cmd.Payload.UnmarshalNew()
		if err != nil {
			b.logger.Warnf("Failed to unmarshal payload: %v", err)
			return
		}
		var msg *waProto.Message
		switch p := payload.(type) {
		case *waProto.Message:
			msg = p
		case *proto.Message:
			msg = (*waProto.Message)(unsafe.Pointer(p))
		default:
			b.logger.Warnf("Invalid payload: %v", payload)
			return
		}

		_, err = b.client.SendMessage(ctx, recipient, msg)
		if err != nil {
			b.logger.Warnf("Failed to send message: %v", err)
			return
		}
	}
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
