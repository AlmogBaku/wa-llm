import re
from typing import List, Generator

from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import WebBaseLoader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter


def find_links(msg: str) -> list[str]:
    pattern = r"(?:(?:https?):\/\/|www\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*" \
              r"(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])"

    return re.findall(pattern, msg, re.IGNORECASE | re.MULTILINE)


class LinkSummary:
    url: str
    title: str
    summary: str

    def __init__(self, url: str, title:str, summary: str):
        self.url = url
        self.title = title
        self.summary = summary


def link_summarizer(links: List[str]) -> Generator[LinkSummary, None, None]:
    if len(links) > 2:
        return

    llm = OpenAI(temperature=0)
    text_splitter = CharacterTextSplitter()

    for link in links:
        loader = WebBaseLoader(link)
        pages = loader.load()
        for page in pages:
            texts = text_splitter.split_text(page.page_content)
            docs = [Document(page_content=t) for t in texts]

            chain = load_summarize_chain(llm, chain_type="map_reduce")
            summary = chain.run(docs)
            yield LinkSummary(url=page.metadata['source'], title=page.metadata['title'], summary=summary)
