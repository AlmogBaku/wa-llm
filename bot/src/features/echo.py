from ..handlers.cmds import CommandResult, msg_cmd
from ..handlers.handler import Instance, Message


@Instance.message_handler
def handle_message(msg: Message) -> CommandResult:
    if not msg.mentioned_me:
        return

    text = msg.text_replace_my_mentions("")

    if text.startswith("/say "):
        yield msg_cmd(msg.chat, text[5:])

    elif text.startswith("/echo "):
        yield msg_cmd(msg.chat, text[6:])
