"""DuckDuckGo search tool with dependency injection."""

from duckduckgo_search import DDGS


class DuckDuckClient:
    """Thin wrapper around ``duckduckgo_search.DDGS`` for DI."""

    def search(self, query: str):
        """Return the first search result for ``query``."""
        with DDGS() as ddgs:
            return ddgs.text(query, max_results=1)


class WebSearchTool:
    """DuckDuckGo search wrapper used by the agent."""

    SCHEMA = {
        "name": "web_search",
        "description": "Perform DuckDuckGo search and return top snippet",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
            },
            "required": ["query"],
        },
    }

    def __init__(self, client: DuckDuckClient | None = None) -> None:
        self.client = client or DuckDuckClient()

    def run(self, args: dict) -> str:
        query = args["query"]
        results = self.client.search(query)
        if not results:
            return "No results"
        r = results[0]
        return f"{r['title']}: {r['body']} ({r['href']})"


# Default instance used by the agent
web_search = WebSearchTool()
