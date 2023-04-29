import uuid
from datetime import datetime
from typing import Generator, Union

from ..jid import JID
from ..proto.msg_event_pb2 import MessageEvent
from ..proto.wa_def_pb2 import Message
from ..proto.wa_handler_pb2 import MessageCmd, Command, AckCmd

CommandResult = Generator[Command, None, None]


def msg_cmd(to: Union[JID, str], msg) -> Command:
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
