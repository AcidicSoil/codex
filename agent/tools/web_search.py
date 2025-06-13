from duckduckgo_search import DDGS

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

def run(args: dict) -> str:
    query = args["query"]
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=1)
        if not results:
            return "No results"
        r = results[0]
        return f"{r['title']}: {r['body']} ({r['href']})"
