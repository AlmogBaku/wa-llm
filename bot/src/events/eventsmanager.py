import contextvars
import inspect
from dataclasses import dataclass
from os.path import basename
from typing import Callable, List, Optional

from loguru import logger

from ..events.cmds import CommandResult, ack_cmd
from ..jid import parse_jid, JID
from ..proto.msg_event_pb2 import MessageEvent
from ..proto.wa_handler_pb2 import Event, AccountContext
from ..proto.wa_handler_pb2_grpc import ChatManagerStub
from ..store.store import ChatStore


class Context:
    """
    Context is a wrapper around contextvars.ContextVar that allows for easier access to context variables.
    """

    context_vars = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, key, value):
        if key == "context_vars":
            raise AttributeError("Cannot set context_vars directly")
        self.__setitem__(key, value)

    def __delattr__(self, item):
        if item == "context_vars":
            raise AttributeError("Cannot delete context_vars directly")
        self.__delitem__(item)

    def __setitem__(self, key, value):
        if key not in self.context_vars:
            self.context_vars[key] = contextvars.ContextVar(key)

        self.context_vars[key].set(value)

    def __getitem__(self, key):
        if key in self.context_vars:
            return self.context_vars[key].get()

    def __delitem__(self, key):
        if key in self.context_vars:
            self.context_vars[key].reset(None)
            del self.context_vars[key]

    def __contains__(self, key):
        return key in self.context_vars

    def __len__(self):
        return len(self.context_vars)


class Message:
    """
    Message is a wrapper around the MessageEvent proto that provides some convenience methods.
    """
    _text: str = ""
    chat: str = None
    my_jid: JID = None
    sender_jid: JID = None
    mentioned_me: bool = False
    raw_message_event: MessageEvent
    raw_account_context: AccountContext
    reply_to: Optional[str] = None

    def __init__(self, event: Event):
        self.raw_message_event = event.message_event
        self.raw_account_context = event.account_context
        self._text = event.message_event.message.conversation
        self.chat = event.message_event.info.message_source.chat

        self.sender_jid, err = parse_jid(event.message_event.info.message_source.sender)
        if err is not None:
            logger.warning(f"Failed to parse sender JID: {err}")

        self.my_jid, err = parse_jid(event.account_context.id)
        if err is not None:
            logger.warning(f"Failed to parse my JID: {err}")

        msg: MessageEvent = event.message_event
        if msg.message.extendedTextMessage is not None:
            if msg.message.extendedTextMessage.contextInfo is not None:
                if msg.message.extendedTextMessage.contextInfo.stanzaId is not None:
                    self.reply_to = msg.message.extendedTextMessage.contextInfo.stanzaId

            if msg.message.conversation == "" and msg.message.extendedTextMessage.text is not None:
                self._text = msg.message.extendedTextMessage.text

            if msg.message.extendedTextMessage.contextInfo is not None:
                if msg.message.extendedTextMessage.contextInfo.mentionedJid is not None and self.my_jid is not None:
                    if self.my_jid.normalize_str() in msg.message.extendedTextMessage.contextInfo.mentionedJid:
                        self.mentioned_me = True

        if self._text == "" and msg.message.reactionMessage is not None and msg.message.reactionMessage.text != '':
            me = str( self.my_jid.to_non_ad())
            if msg.message.reactionMessage.key.remoteJid !=  me and msg.message.reactionMessage.key.participant != me:  # don't handle reactions to my own messages
                self._text = msg.message.reactionMessage.text
                self.reply_to = msg.message.reactionMessage.key.id

    @property
    def text(self) -> str:
        return self._text.strip()

    def text_replace_my_mentions(self, replacement: str) -> str:
        return self.text.replace(f"@{self.my_jid.user}", replacement).strip()


MessageHandler = Callable[[Context, Message], CommandResult]
_message_handlers: List[MessageHandler] = []


def message_handler(handler: MessageHandler) -> MessageHandler:
    """
    Registers a message handler.

    :param handler: a function that takes a Message object and (might) generates a CommandResult.
    :return: the same handler that was passed in.
    """
    global _message_handlers
    _message_handlers.append(handler)
    return handler


@dataclass(frozen=True, eq=False)
class EventsManager:
    """
    EventsManager is an event handler that handles incoming events from the chat-manager and dispatches them to the
    appropriate handlers.
    """
    store: ChatStore = None
    stub: ChatManagerStub = None

    def handle(self, event: Event) -> CommandResult:
        if event.message_event is not None:
            ctx = Context(store=self.store, stub=self.stub)
            yield from self._handle_message(ctx, Message(event))
            yield ack_cmd(event.message_event)

    # Message handling
    @staticmethod
    def _handle_message(ctx: Context, msg: Message) -> CommandResult:
        logger.debug(f"Got message: {msg.text}")
        logger.debug(f"Was I mentioned? {msg.mentioned_me}")
        if msg.text == "":
            logger.debug("got empty message", msg)
            logger.debug(msg)

        for handler in _message_handlers:
            logger.debug(f"Calling handler {basename(inspect.getfile(handler))}#{handler.__name__}()")
            try:
                res = handler(ctx, msg)
                if res is not None:
                    yield from handler(ctx, msg)
            except Exception as e:
                logger.exception(f"Error while calling message handler {handler}: {e}")
                raise e
