package manager

import (
	"chat-manager/proto"
	"github.com/google/uuid"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/types/events"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/protobuf/types/known/timestamppb"
	"time"
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
			if e == nil {
				continue
			}
			if e.Timestamp.AsTime().Before(time.Now().Add(-10 * time.Minute)) {
				m.logger.Warnf("Skipping event %s, too old", e.Uuid)
				continue
			}
			e.SubscriptionId = sr.Uuid
			err := stream.Send(e)
			if err != nil {
				m.logger.Errorf("failed to send event: %w", err)
			}
		case <-stream.Context().Done():
			return nil
		}
	}

}

func (m *mgr) publishEvent(e any) {
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
