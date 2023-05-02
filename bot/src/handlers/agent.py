import re
from datetime import datetime

from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType, tool, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.schema import OutputParserException
from langchain.tools import BaseTool

from ..events import Context, CommandResult, msg_cmd, Message, message_handler
from ..jid import JID, DefaultUserServer
from ..store import ChatStore


@message_handler
def handle_message(ctx: Context, msg: Message) -> CommandResult:
    if not msg.mentioned_me:
        return

    txt = msg.text_replace_my_mentions("")

    cmd = '!'
    if not txt.startswith(cmd):
        return

    txt = txt[len(cmd):].strip()
    if txt == "":
        return

    llm1 = OpenAI(temperature=0)
    llm = ChatOpenAI(temperature=0)

    tools = load_tools(["requests_all", "llm-math", "open-meteo-api", "wikipedia"], llm=llm1)
    tools += [
        ChatHistoryTool(store=ctx.store, chat_jid=msg.chat, my_jid=msg.my_jid),
        say,
        today,
        date_difference,
    ]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    try:
        response = agent.run(txt)
    except OutputParserException as e:
        response = str(e)

        pattern = r'say\("([^"]*)"\)'
        match = re.search(pattern, response)
        if match:
            response = match.group(1)
    yield msg_cmd(msg.chat, response)


@tool
def say(text: str) -> str:
    """Say what you want to say. This is a tool that can be used by the agent when it wants to say, write or speak
    something."""
    return text


@tool
def today(text: str) -> str:
    """Get today's date and time information.
    You MUST use this tool every time you want to get today's date or time information."""
    return (f"Today is {datetime.now().strftime('%A %d %B %Y')} and the time is {datetime.now().strftime('%H:%M')}\n"
            f"In ISO format this is {datetime.now().isoformat()}")


@tool
def date_difference(text: str) -> str:
    """Return the difference between two dates in seconds.
    You MUST use this tool every time you want to get the difference between two dates or times.
    This is useful for when you want to know how long it has been since something happened, or find out how long it will
    be until something happens, or how long it has been since something happened.

    The input to this tool is a comma separated start and end time in ISO format. For example:
    `2021-01-01T00:00:00,2021-01-01T23:59:59` would mean you want to see the difference between the 1-1-2021 00:00 and 1-1-2021 23:59.
    """

    start, end = text.strip().split(",")
    start = datetime.fromisoformat(start.strip())
    end = datetime.fromisoformat(end.strip())
    return str((end - start).total_seconds())


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
