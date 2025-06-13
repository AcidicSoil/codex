#!/usr/bin/env python3
from openai import OpenAI
from agent.config import settings
from agent.tools import python_exec, git_status, web_search

TOOLS = [t.SCHEMA for t in (python_exec, git_status, web_search)]
TOOL_MAP = {
    python_exec.SCHEMA["name"]: python_exec,
    git_status.SCHEMA["name"]: git_status,
    web_search.SCHEMA["name"]: web_search,
}

client = OpenAI(base_url=settings.api_base, api_key=settings.api_key)

history = [{"role": "system", "content": "You are an efficient DevOps assistant."}]

def call_llm(messages, tools=None, stream=False):
    return client.chat.completions.create(
        model=settings.model,
        messages=messages,
        tools=tools,
        stream=stream,
    )


def main():
    user_prompt = input("\u276f ")
    history.append({"role": "user", "content": user_prompt})

    for _ in range(settings.max_iter):
        resp = call_llm(history, tools=TOOLS)
        msg = resp.choices[0].message

        if msg.tool_calls:
            for tc in msg.tool_calls:
                name = tc.function.name
                args = tc.function.arguments
                result = TOOL_MAP[name].run(args)
                history.extend([
                    {"role": "assistant", "tool_call_id": tc.id, **tc.to_dict()},
                    {"role": "tool", "tool_call_id": tc.id, "content": result},
                ])
            continue

        final = call_llm(history, tools=None, stream=True)
        for chunk in final:
            print(chunk.choices[0].delta.content or "", end="", flush=True)
        print()
        break
    else:
        print("\u26d4 Max iterations reached \u2014 aborting.")

if __name__ == "__main__":
    main()
