import logging
from typing import Iterator

from grpc import ServicerContext, StatusCode

from proto import wa_handler_pb2, wa_handler_pb2_grpc
from python.cmds import msg_cmd, CommandResult
from python.links import find_links, link_summarizer


class HandlerServicer(wa_handler_pb2_grpc.HandlerServicer):
    def attach_to_server(self, server):
        wa_handler_pb2_grpc.add_HandlerServicer_to_server(self, server)

    @staticmethod
    def full_name():
        return wa_handler_pb2.DESCRIPTOR.services_by_name[wa_handler_pb2_grpc.Handler.__name__].full_name

    def Handle(self, request_iterator: Iterator[wa_handler_pb2.Event], context: ServicerContext):
        for event in request_iterator:
            try:
                if event.message_event is not None:
                    yield from self.handle_message(event, context)
            except Exception as e:
                logging.error(f'Got exception', e)
                context.abort(StatusCode.INTERNAL, str(e))

    # Message handling

    @staticmethod
    def handle_message(evnt: wa_handler_pb2.Event, context: ServicerContext) -> CommandResult:
        msg = evnt.message_event

        txt = msg.message.conversation
        if txt is None or txt == "" and msg.message.extendedTextMessage is not None:
            txt = msg.message.extendedTextMessage.text
        print(f"Got message: {txt}")

        links = find_links(txt)
        if len(links) > 0:
            print(f"Found {len(links)} links")
            for summary in link_summarizer(links):
                yield msg_cmd(msg.info.message_source.chat,
                              f"Yo, a quick summary for {summary.url}:\n{summary.summary}")

        if msg.message.conversation.startswith("/echo "):
            yield msg_cmd(msg.info.message_source.chat, msg.message.conversation[6:])
