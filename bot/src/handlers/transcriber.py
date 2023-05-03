import os
import shutil
from functools import lru_cache

import ffmpeg
import numpy as np
from loguru import logger
from whispercpp import Whisper

from ..events import message_handler, Context, CommandResult, Message, download_cmd, msg_cmd
from ..jid import parse_jid
from ..proto.wa_handler_pb2 import CommandResponse
from ..proto.wa_handler_pb2_grpc import ChatManagerStub
from ..store import ChatStore

_model: Whisper | None = None


@lru_cache(maxsize=1)
def get_model() -> Whisper:
    _MODEL_NAME = os.environ.get("GGML_MODEL", "tiny")

    global _model
    if _model is None:
        _model = Whisper.from_pretrained(_MODEL_NAME)
    return _model


@message_handler
def handle_message(ctx: Context, msg: Message) -> CommandResult:
    chat_jid, err = parse_jid(msg.chat)
    if err is not None:
        logger.warning(f"Failed to parse chat JID: {err}")
        return

    if chat_jid.is_group():
        store: ChatStore = ctx.store
        group = store.get_group(chat_jid)
        if group is None:
            logger.warning(f"Failed to get group {chat_jid}: {err}")
            return

        if not group.managed:
            logger.debug(f"Group {chat_jid} is not managed, but found a link. Ignoring.")
            return

    if msg.raw_message_event.info.type != "media" or msg.raw_message_event.info.media_type != "ptt":
        return

    if msg.raw_message_event.message.audioMessage is None or msg.raw_message_event.message.audioMessage.url is None or \
            msg.raw_message_event.message.audioMessage.url == "":
        logger.warning(f"Invalid audio message: {msg.raw_message_event}")
        return

    stub: ChatManagerStub = ctx.stub
    resp: CommandResponse = stub.Execute(download_cmd(msg.raw_message_event))
    if resp.download_response is None:
        logger.warning(f"Failed to download message {msg.raw_message_event.info.id}: {resp.error}")
        return

    if resp.download_response.message_id != msg.raw_message_event.info.id or resp.download_response.file_uri is None:
        logger.warning(f"Failed to download message {msg.raw_message_event.info.id}: {resp.error}")
        return

    file = resp.download_response.file_uri
    if not file.startswith("file://"):
        logger.warning(f"Invalid file uri: {file}")
        return

    file = file[len("file://"):]

    new_dir = shutil.move(file, file.replace(".enc", "") + ".ogg")

    try:
        y, _ = (
            ffmpeg.input(new_dir, threads=0)
            .output("-", format="s16le", acodec="pcm_s16le", ar=16000)
            .run(
                cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True
            )
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    arr = np.frombuffer(y, np.int16).flatten().astype(np.float32) / 32768.0

    w = get_model()
    w.params = w.params.with_language("auto")
    ret = w.transcribe(arr)
    yield msg_cmd(msg.chat, f"@{msg.sender_jid.user} said:\n{ret}", reply_to=msg.raw_message_event)
