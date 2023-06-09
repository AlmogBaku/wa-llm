from datetime import timedelta

from ..events import Context, CommandResult, msg_cmd, Message, message_handler


@message_handler
def handle_message(ctx: Context, msg: Message) -> CommandResult:
    if msg.sent_before(timedelta(minutes=30)):
        return

    if not msg.mentioned_me:
        return

    text = msg.text_replace_my_mentions("")

    if text.startswith("/say "):
        yield msg_cmd(msg.chat, text[5:])

    elif text.startswith("/echo "):
        yield msg_cmd(msg.chat, text[6:])
