import re
from datetime import datetime

from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models.base import BaseChatModel
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.tools import BaseTool

from ...jid import JID, DefaultUserServer
from ...store import ChatStore


class SummarizeChatHistory(BaseTool):
    name = "summarize_chat_history"
    description = (
        "Summarize a chat history."
        "You MUST use this tool every time you want to get a summary of a chat or know the history of a chat. "
        "This is useful for when you want to summarize what was discussed in a chat, get the main idea of a chat, "
        "learn what was discussed in a chat, catch up on a group chat you haven't been in for a while, or want to "
        "know what we discussed in a group chat."
        "The input to this tool is a comma separated start and end time in ISO format. If you don't know the time use "
        "None. For example: `2021-01-01T00:00:00,2021-01-01T23:59:59` would mean you want to see the chat history "
        "from the 1-1-2021 00:00 to 1-1-2021 23:59."
    )

    prompt_template = """Write a concise summary of the following group chat history by the different topics discussed:


"{text}"


CONCISE SUMMARY:"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])

    llm: BaseChatModel
    store: ChatStore
    chat_jid: str
    my_jid: JID

    def _run(self, query: str) -> str:
        """Use the tool."""

        start_of_today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_today = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)

        times = query.strip().split(",")
        if len(times) == 2:
            if times[0].title() != "None":
                start_of_today = datetime.fromisoformat(times[0].strip())
            if times[1].title() != "None":
                end_of_today = datetime.fromisoformat(times[1].strip())

        msgs = self.store.fetch_messages(self.chat_jid, start_of_today, end_of_today)

        if len(msgs) == 0:
            return "No messages found in the given time period. Is the time period correct?"

        txt = "\n".join([f"{msg.sender.push_name}: {msg.text}" for msg in msgs])
        txt = txt.replace(f"@{self.my_jid.user}", "@Bot")

        mentions = re.findall(r"@(\d{7,15})", txt, re.MULTILINE)
        mentions_push = {}
        for mention in mentions:
            if mention not in mentions_push:
                sender = self.store.get_sender(jid=JID(user=mention, server=DefaultUserServer))
                if sender is not None:
                    mentions_push[mention] = sender.push_name

        for mention in mentions_push:
            txt = txt.replace(mention, f"@{mentions_push[mention]}")

        chain = load_summarize_chain(self.llm, chain_type="map_reduce", map_prompt=self.PROMPT,
                                     combine_prompt=self.PROMPT)

        text_splitter = CharacterTextSplitter.from_tiktoken_encoder()
        olf = text_splitter._length_function
        text_splitter._length_function = lambda x: olf(x) + olf(self.prompt_template)

        texts = text_splitter.split_text(txt)
        docs = [Document(page_content=t) for t in texts]
        summary = chain.run(docs)
        return summary

    async def _arun(self, query: str) -> str:
        return self._run(query)
