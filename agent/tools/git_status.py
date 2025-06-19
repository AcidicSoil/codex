import subprocess

SCHEMA = {
    "name": "git_status",
    "description": "Return clean/dirty git tree summary",
    "parameters": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Path to repo", "default": "."},
        },
        "required": [],
    },
}

def run(args: dict) -> str:
    path = args.get("path", ".")
    out = subprocess.check_output(["git", "status", "-s", path], text=True)
    return out
