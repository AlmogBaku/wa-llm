import re
from datetime import datetime

from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import BaseTool

from ..events import Context, CommandResult, msg_cmd, Message, message_handler
from ..jid import JID, DefaultUserServer
from ..store import ChatStore


@message_handler
def handle_message(ctx: Context, msg: Message) -> CommandResult:
    if not msg.mentioned_me:
        return

    txt = msg.text_replace_my_mentions("")

    if not txt.startswith("/ask "):
        return

    txt = txt[len("/ask "):]

    llm = OpenAI(temperature=0)
    agent = initialize_agent([
        ChatHistoryTool(store=ctx.store, chat_jid=msg.chat, my_jid=msg.my_jid),
    ], llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    response = agent.run(txt)
    yield msg_cmd(msg.chat, response)


class ChatHistoryTool(BaseTool):
    name = "chat_history"
    description = (
        "Fetch the history of a group chat today."
        "Call this tool when you want to get today's chat history of a group chat."
        "This is useful for when you want to catch up on a group chat you haven't been in for a while."
        "This is also useful if you want to see what you missed while you were gone."
        "The input to this tool is a comma separated start and end time in ISO format. If you don't know the time use "
        "None. For example: `2021-01-01T00:00:00,2021-01-01T23:59:59` would mean you want to see the chat history "
        "from the 1-1-2021 00:00 to 1-1-2021 23:59."
        f"today is the `{datetime.now().isoformat()}`"
    )
    store: ChatStore
    chat_jid: str
    my_jid: JID

    def _run(self, query: str) -> str:
        """Use the tool."""

        start_of_today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_today = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)

        times = query.split(",")
        if len(times) == 2:
            if times[0].title() != "None":
                start_of_today = datetime.fromisoformat(times[0])
            if times[1].title() != "None":
                end_of_today = datetime.fromisoformat(times[1])

        msgs = self.store.fetch_messages(self.chat_jid, start_of_today, end_of_today)

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
        return txt

    async def _arun(self, query: str) -> str:
        return self._run(query)
