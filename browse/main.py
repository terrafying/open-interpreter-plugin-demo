from .plugin import InterpreterPlugin

plugin = InterpreterPlugin("browser")


def search(self, query):
    return {"results": ["result 1", "result 2", "result 3", "result 4", "result 5"]}


def browse(self, url):
    return {
        "title": "Page Title",
        "content": "<html><body><h1>Page Content</h1></body></html>",
    }


print("Registering search function...")

plugin.register_function(
    {
        "name": "search",
        "description": "Searches Google for the given query and returns the top 5 results",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search for (required parameter to the `search` function)",
                },
            },
            "required": ["query"],
        },
    },
    function=search,
)

print("Registering browse function...")

plugin.register_function(
    {
        "name": "browse",
        "description": "Navigate to a webpage in a headless browser, render the page content, and return the title of the page and the content of the page as HTML for parsing",
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
