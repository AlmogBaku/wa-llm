from loguru import logger
from uuid import uuid4

import grpc

from .events import EventsManager
from .proto.wa_handler_pb2 import SubscribeRequest
from .proto.wa_handler_pb2_grpc import ChatManagerStub
from .store.store import ChatStore


def start_bot(channel: grpc.Channel, store: ChatStore) -> None:
    stub = ChatManagerStub(channel)
    handler = EventsManager(store, stub)

    logger.info("Subscribing to events...")
    for event in stub.Subscribe(SubscribeRequest(uuid=uuid4().hex)):
        for cmd in handler.handle(event):
            stub.Execute(cmd)
