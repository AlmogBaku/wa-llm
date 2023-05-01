import re
import uuid
from datetime import datetime
from typing import Generator, Union, Optional

from ..jid import JID, DefaultUserServer
from ..proto.msg_event_pb2 import MessageEvent
from ..proto.wa_def_pb2 import Message, ExtendedTextMessage, ContextInfo
from ..proto.wa_handler_pb2 import MessageCmd, Command, AckCmd, GroupInfoCmd, DownloadCmd

CommandResult = Optional[Generator[Command, None, None]]


def msg_cmd(to: Union[JID, str], msg, reply_to: Optional[MessageEvent] = None) -> Command:
    mentions = re.findall(r"@(\d{7,15})", msg, re.MULTILINE)
    mentions = [str(JID(user_id, server=DefaultUserServer)) for user_id in mentions]

    reply_to = None  # todo: fix this
    if reply_to is not None:
        return Command(
            uuid=uuid.uuid4().hex,
            message_cmd=MessageCmd(
                to=to,
                message=Message(extendedTextMessage=ExtendedTextMessage(
                    text=msg,
                    contextInfo=ContextInfo(
                        stanzaId=reply_to.info.id,
                        participant=reply_to.info.message_source.sender,
                        quotedMessage=reply_to.message,
                        mentionedJid=mentions,
                    ),
                )),
            ),
        )

    if len(mentions) > 0:
        return Command(
            uuid=uuid.uuid4().hex,
            message_cmd=MessageCmd(
                to=to,
                message=Message(extendedTextMessage=ExtendedTextMessage(
                    text=msg,
                    contextInfo=ContextInfo(
                        mentionedJid=mentions,
                    ),
                )),
            ),
        )

    return Command(
        uuid=uuid.uuid4().hex,
        message_cmd=MessageCmd(
            to=to,
            message=Message(conversation=msg),
        ),
    )


def ack_cmd(message_event: MessageEvent) -> Command:
    ack = AckCmd(
        message_ids=[message_event.info.id],
        chat_jid=message_event.info.message_source.chat,
        sender_jid=message_event.info.message_source.sender,
    )
    ack.timestamp.FromDatetime(datetime.now())
    return Command(
        uuid=uuid.uuid4().hex,
        ack_cmd=ack,
    )


def group_info_cmd(jid: Union[JID, str]) -> Command:
    return Command(
        uuid=uuid.uuid4().hex,
        group_info_cmd=GroupInfoCmd(
            jid=str(jid),
        ),
    )


def download_cmd(message_event: MessageEvent) -> Command:
    cmd = DownloadCmd(
        message_id=message_event.info.id,
        chat_jid=message_event.info.message_source.chat,
    )

    if message_event.message.audioMessage is not None:
        cmd.audio_message.CopyFrom(message_event.message.audioMessage)
    elif message_event.message.videoMessage is not None:
        cmd.video_message.CopyFrom(message_event.message.videoMessage)
    elif message_event.message.imageMessage is not None:
        cmd.image_message.CopyFrom(message_event.message.imageMessage)
    elif message_event.message.documentMessage is not None:
        cmd.document_message.CopyFrom(message_event.message.documentMessage)
    elif message_event.message.stickerMessage is not None:
        cmd.sticker_message.CopyFrom(message_event.message.stickerMessage)
    else:
        raise ValueError("Message type not supported")

    return Command(
        uuid=uuid.uuid4().hex,
        download_cmd=cmd,
    )
