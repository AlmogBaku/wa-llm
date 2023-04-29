import re
from typing import List, Generator

from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PlaywrightURLLoader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter

from ..events.cmds import CommandResult, msg_cmd
from ..events.handler import Message, Instance


def find_links(msg: str) -> list[str]:
    pattern = r"(?:(?:https?):\/\/|www\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*" \
              r"(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])"

    return re.findall(pattern, msg, re.IGNORECASE | re.MULTILINE)


class LinkSummary:
    url: str
    summary: str

    def __init__(self, url: str, summary: str):
        self.url = url
        self.summary = summary


def link_summarizer(links: List[str]) -> Generator[LinkSummary, None, None]:
    if len(links) > 2:
        return

    # Add "http://" if the scheme is missing from the URL
    links = [l if l.startswith("http") else f"http://{l}" for l in links]

    llm = OpenAI(temperature=0)
    text_splitter = CharacterTextSplitter()

    loader = PlaywrightURLLoader(urls=links, remove_selectors=["header", "footer", "script", "style", "iframe", "nav"])
    pages = loader.load()

    print(f"Got {len(pages)} pages")
    for page in pages:
        texts = text_splitter.split_text(page.page_content)
        docs = [Document(page_content=t) for t in texts]

        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)
        yield LinkSummary(url=page.metadata['source'], summary=summary)


@Instance.message_handler
def handle_message(msg: Message) -> CommandResult:
    links = find_links(msg.text)
    if len(links) > 0:
        print(f"Found {len(links)} links")
        for summary in link_summarizer(links):
            yield msg_cmd(msg.chat, f"Yo, a quick summary for {summary.url}:\n{summary.summary}")
