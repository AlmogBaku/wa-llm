import os
from io import BytesIO

import ffmpeg
import openai
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from loguru import logger

from ..events import message_handler, Context, CommandResult, Message, download_cmd, msg_cmd
from ..jid import parse_jid
from ..proto.wa_handler_pb2 import CommandResponse
from ..proto.wa_handler_pb2_grpc import ChatManagerStub
from ..store import ChatStore


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

    if resp.download_response.message_id != msg.raw_message_event.info.id or resp.download_response.data is None:
        logger.warning(f"Failed to download message {msg.raw_message_event.info.id}: {resp.error}")
        return

    try:
        mp3bytes, _ = (
            ffmpeg.input("pipe:", format="ogg", acodec="libopus")
            .output("-", format="mp3", acodec='libmp3lame', ac=1, ar=16000, ab="32k",
                    af="asendcmd=c='0.0 afftdn@n sn start; 1.0 afftdn@n sn stop',afftdn@n")
            .run(
                cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True, input=resp.download_response.data
            )
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    mp3 = BytesIO(mp3bytes)
    mp3.name = f"{resp.download_response.message_id}.mp3"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    transcription = openai.Audio.transcribe("whisper-1", mp3)
    if transcription.text is None or transcription.text == "":
        logger.warning(f"Failed to transcribe audio: {transcription}")
        return

    if len(transcription.text.split(" ")) < 3:
        yield msg_cmd(msg.chat, f"@{msg.sender_jid.user} said:\n{transcription.text}", reply_to=msg.raw_message_event)
        return

    llm = ChatOpenAI(temperature=0)
    prompt = PromptTemplate(
        input_variables=["transcription"],
        template=(
            "Return a formatted, punctuated, splitted to paragraph, and fixed transcription WITHOUT changing, adding "
            "or removing anything. DO NOT wrap it with quotes or add any comments/notes/explanations.\n\n"
            "{transcription}"
        )
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(transcription.text)

    yield msg_cmd(msg.chat, f"@{msg.sender_jid.user} said:\n{result}", reply_to=msg.raw_message_event)
