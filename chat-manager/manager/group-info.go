package manager

import (
	"context"
	"fmt"
	"google.golang.org/protobuf/types/known/timestamppb"
)

import (
	"chat-manager/proto"
	"go.mau.fi/whatsmeow/types"
)

func (m *mgr) groupInfoCmd(ctx context.Context, cmd *proto.Command) (*proto.CommandResponse, error) {
	jid, err := types.ParseJID(cmd.GetGroupInfoCmd().GetJid())
	if err != nil {
		m.logger.Warnf("Failed to parse jid: %w", err)
		return nil, fmt.Errorf("failed to parse jid: %w", err)
	}

	info, err := m.client.GetGroupInfo(jid)
	if err != nil {
		m.logger.Warnf("Failed to get group info: %w", err)
		return nil, fmt.Errorf("failed to get group info: %w", err)
	}

	protoInfo, err := groupInfoToProto(info)
	if err != nil {
		m.logger.Warnf("Failed to convert group info: %w", err)
		return nil, fmt.Errorf("failed to convert group info: %w", err)
	}

	return &proto.CommandResponse{Uuid: cmd.Uuid, Response: &proto.CommandResponse_GroupInfo{GroupInfo: protoInfo}}, nil
}

func groupInfoToProto(info *types.GroupInfo) (*proto.GroupInfo, error) {
	participantsProto := make([]*proto.GroupParticipantEnriched, len(info.Participants))
	for i, participant := range info.Participants {
		participantsProto[i] = &proto.GroupParticipantEnriched{
			Jid:          participant.JID.String(),
			IsAdmin:      participant.IsAdmin,
			IsSuperAdmin: participant.IsSuperAdmin,
		}
	}

	return &proto.GroupInfo{
		Jid:      info.JID.String(),
		OwnerJid: info.OwnerJID.String(),
		GroupName: &proto.GroupName{
			Name:      info.GroupName.Name,
			NameSetAt: timestamppb.New(info.GroupName.NameSetAt),
			NameSetBy: info.GroupName.NameSetBy.String(),
		},
		GroupTopic: &proto.GroupTopic{
			Topic:        info.GroupTopic.Topic,
			TopicId:      info.GroupTopic.TopicID,
			TopicSetAt:   timestamppb.New(info.GroupTopic.TopicSetAt),
			TopicSetBy:   info.GroupTopic.TopicSetBy.String(),
			TopicDeleted: info.GroupTopic.TopicDeleted,
		},
		GroupLocked: &proto.GroupLocked{
			IsLocked: info.GroupLocked.IsLocked,
		},
		GroupAnnounce: &proto.GroupAnnounce{
			IsAnnounce:        info.GroupAnnounce.IsAnnounce,
			AnnounceVersionId: info.GroupAnnounce.AnnounceVersionID,
		},
		GroupEphemeral: &proto.GroupEphemeral{
			IsEphemeral:       info.GroupEphemeral.IsEphemeral,
			DisappearingTimer: info.GroupEphemeral.DisappearingTimer,
		},
		GroupParent: &proto.GroupParent{
			IsParent:                      info.GroupParent.IsParent,
			DefaultMembershipApprovalMode: info.GroupParent.DefaultMembershipApprovalMode,
		},
		GroupLinkedParent: &proto.GroupLinkedParent{
			LinkedParentJid: info.GroupLinkedParent.LinkedParentJID.String(),
		},
		GroupIsDefaultSub: &proto.GroupIsDefaultSub{
			IsDefaultSubGroup: info.GroupIsDefaultSub.IsDefaultSubGroup,
		},
		GroupCreated:         timestamppb.New(info.GroupCreated),
		ParticipantVersionId: info.ParticipantVersionID,
		Participants:         participantsProto,
		MemberAddMode:        string(info.MemberAddMode),
	}, nil
}
