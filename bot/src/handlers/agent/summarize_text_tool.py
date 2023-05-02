from langchain.chains.summarize import load_summarize_chain
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain.chat_models.base import BaseChatModel
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.tools import BaseTool


class SummarizeText(BaseTool):
    llm: BaseChatModel
    name = "summarize_text"
    description = (
        "Summarize a text."
        "You MUST use this tool every time you want to summarize a text. This is useful for when you want to summarize "
        "a long text into a short text.  This is also useful when you have a text you want to make more concise, or "
        "when you want to get the main idea of a text."
    )

    def _run(self, text: str) -> str:
        chain = load_summarize_chain(self.llm, chain_type="map_reduce")

        text_splitter = CharacterTextSplitter.from_tiktoken_encoder()
        olf = text_splitter._length_function
        text_splitter._length_function = lambda x: olf(x) + olf(prompt_template)

        texts = text_splitter.split_text(text)
        docs = [Document(page_content=t) for t in texts]
        summary = chain.run(docs)
        return summary

    async def _arun(self, query: str) -> str:
        return self._run(query)