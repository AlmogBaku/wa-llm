import asyncio
from threading import Thread

from loguru import logger

from ..events import Context, CommandResult, Message, message_handler, group_info_cmd
from ..jid import parse_jid, JID
from ..proto.wa_group_pb2 import GroupInfo
from ..proto.wa_handler_pb2 import CommandResponse
from ..proto.wa_handler_pb2_grpc import ChatManagerStub
from ..store import ChatStore


async def save_message(store, msg):
    rply = None
    em = msg.raw_message_event.message.extendedTextMessage
    if em is not None:
        if em.contextInfo is not None:
            if em.contextInfo.stanzaId is not None:
                rply = em.contextInfo.stanzaId

    store.save_message(
        timestamp=msg.raw_message_event.info.timestamp.ToDatetime(),
        message_id=msg.raw_message_event.info.id,
        chat_jid=msg.raw_message_event.info.message_source.chat,
        sender_jid=msg.raw_message_event.info.message_source.sender,
        sender_push_name=msg.raw_message_event.info.push_name,
        text=msg.text,
        reply_to=rply,
    )


async def save_group(stub: ChatManagerStub, store: ChatStore, chat_jid: JID):
    gr: CommandResponse = stub.Execute(group_info_cmd(chat_jid))
    if gr.group_info is None or gr.group_info.jid == chat_jid:
        raise ValueError(f"Failed to get group info for {chat_jid}")

    store.save_group(
        group_jid=gr.group_info.jid,
        group_name=gr.group_info.group_name.name,
        group_topic=gr.group_info.group_topic.topic,
        owner_jid=gr.group_info.owner_jid,
    )


def run_async_tasks(*coroutines):
    def run_in_new_loop(coros):
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = [loop.create_task(coro) for coro in coros]
        try:
            loop.run_until_complete(asyncio.gather(*tasks))
        finally:
            loop.close()

    new_loop_thread = Thread(target=run_in_new_loop, args=(coroutines,))
    new_loop_thread.start()


@message_handler
def handle_message(ctx: Context, msg: Message) -> CommandResult:
    store: ChatStore = ctx.store
    stub: ChatManagerStub = ctx.stub
    if store is None:
        logger.warning("Store not found in context")
        return

    coroutines = [save_message(store, msg)]

    chat_jid, err = parse_jid(msg.raw_message_event.info.message_source.chat)
    if err is not None:
        logger.warning(f"Failed to parse chat jid: {err}")
        return

    if chat_jid.is_group():
        group = store.get_group(str(chat_jid))
        if not group:
            coroutines.append(save_group(stub, store, chat_jid))

    run_async_tasks(*coroutines)
