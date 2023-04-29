from typing import Callable, List
from warnings import warn

from ..handler.cmds import CommandResult, ack_cmd
from ..jid import parse_jid, JID
from ..proto.wa_handler_pb2 import Event, AccountContext, MessageEvent


class Message:
    _text: str = ""
    chat: str = None
    my_jid: JID = None
    mentioned_me: bool = False
    raw_message_event: MessageEvent
    raw_account_context: AccountContext

    def __init__(self, event: Event):
        self._text = event.message_event.message.conversation
        self.chat = event.message_event.info.message_source.chat

        self.my_jid, err = parse_jid(event.account_context.id)
        if err is not None:
            warn(f"Failed to parse my JID: {err}")

        msg = event.message_event
        if msg.message.extendedTextMessage is not None:
            if msg.message.conversation == "" and msg.message.extendedTextMessage.text is not None:
                self._text = msg.message.extendedTextMessage.text

            if msg.message.extendedTextMessage.contextInfo is not None:
                if msg.message.extendedTextMessage.contextInfo.mentionedJid is not None and self.my_jid is not None:
                    if str(self.my_jid.to_non_ad()) in msg.message.extendedTextMessage.contextInfo.mentionedJid:
                        self.mentioned_me = True

    @property
    def text(self) -> str:
        return self._text.strip()

    def text_replace_my_mentions(self, replacement: str) -> str:
        return self.text.replace(f"@{self.my_jid.user}", replacement).strip()


MessageHandler = Callable[[Message], CommandResult]


class Handler(object):
    _message_handlers: List[MessageHandler] = []

    def message_handler(self, handler: MessageHandler) -> MessageHandler:
        self._message_handlers.append(handler)
        return handler

    def handle(self, event: Event) -> CommandResult:
        if event.message_event is not None:
            yield from self._handle_message(Message(event))
            yield ack_cmd(event.message_event)

    # Message handling

    def _handle_message(self, msg: Message) -> CommandResult:
        print(f"Got message: {msg.text}")
        print(f"Was I mentioned? {msg.mentioned_me}")

        for handler in self._message_handlers:
            yield from handler(msg)


Instance = Handler()
