import uuid
from typing import Generator

from google.protobuf import any_pb2

from python.proto import wa_def_pb2, wa_handler_pb2

CommandResult = Generator[wa_handler_pb2.Command, None, None]


def msg_cmd(recipient, msg):
    payload = any_pb2.Any()
    payload.Pack(wa_def_pb2.Message(conversation=msg))

    return wa_handler_pb2.Command(
        uuid=uuid.uuid4().hex,
        action=wa_handler_pb2.Command.Action.SEND_MESSAGE,
        recipient=recipient,
        payload=payload
    )
