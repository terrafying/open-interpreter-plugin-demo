import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

from .plugin import InterpreterPlugin

plugin = InterpreterPlugin("browser")


def browse(self, url=""):
    page_request = requests.get(url)

    page = BeautifulSoup(page_request.text, "html.parser")

    title = page.title.string

    body = page.body

    [element.extract() for element in page(['iframe', 'script'])]

    content = md("".join(str(item) for item in body.contents))

    content = re.sub(r"\n\s+", "\n", content).strip()

    return f"""
    The content of {url} is:

    ```markdown
    # {title}

    {content}
    ```
    """


plugin.register_function(
    {
        "name": "browse",
        "description": "Scrape the content from the provided URL and return the title of the page and the content of the page as a Markdown document.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The url of the webpage to navigate to (required parameter to the `browse` function)",
                },
            },
            "required": ["url"],
        },
    },
    function=browse,
)
