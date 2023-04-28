from dotenv import load_dotenv

from python.links import find_links, link_summarizer

load_dotenv()

text = "maybe this will help https://bobbyhadz.com/blog/python-runtimeerror-dictionary-changed-size-during-iteration"

links = find_links(text)

for summary in link_summarizer(links):
    print(summary.url)
    print(summary.summary)
    print()