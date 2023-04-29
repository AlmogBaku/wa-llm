package manager

import (
	"chat-manager/proto"
	"go.mau.fi/whatsmeow/types/events"
	"google.golang.org/protobuf/types/known/timestamppb"
	"unsafe"
)

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
