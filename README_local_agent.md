# Local Codex-Style Agent

This example demonstrates a lightweight tool-calling loop that works with a local OpenAI-compatible LLM endpoint (e.g. LM Studio running Qwen3). It shows how to register JSON-schema tools, execute them securely, and stream responses.

## Setup

1. Install Python dependencies

```bash
pip install -r requirements.txt
```

2. Copy `.env.template` to `.env` and adjust values for your local model server.

3. Run the agent

```bash
python codex_local_shell_bridge.py
```

## Files

- `agent/config.py` — loads settings from environment variables
- `agent/tools/` — collection of simple tools (`python_exec`, `git_status`, `web_search`)
- `agent/main.py` — the main ReAct loop handling tool calls
- `codex_local_shell_bridge.py` — convenience entry point

## Testing

Run unit tests with `pytest`:

```bash
pytest
```
