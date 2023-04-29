package manager

import (
	"go.mau.fi/whatsmeow/appstate"
	"go.mau.fi/whatsmeow/types"
	"go.mau.fi/whatsmeow/types/events"
	"os"
)

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

	m.publishEvent(msg)
}
