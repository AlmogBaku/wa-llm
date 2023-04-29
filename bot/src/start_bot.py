import logging
from uuid import uuid4

import grpc

from .handler.handler import Instance as HandlerInstance
from .proto.wa_handler_pb2 import SubscribeRequest
from .proto.wa_handler_pb2_grpc import ChatManagerStub


def start_bot(channel: grpc.Channel) -> None:
    stub = ChatManagerStub(channel)

    logging.info("Subscribing to events...")
    for event in stub.Subscribe(SubscribeRequest(uuid=uuid4().hex)):
        for cmd in HandlerInstance.handle(event):
            stub.Execute(cmd)
