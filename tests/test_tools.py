import os

os.environ.setdefault("OPENAI_API_BASE", "http://localhost:1234/v1")
os.environ.setdefault("OPENAI_API_KEY", "test-key")
os.environ.setdefault("MODEL_NAME", "dummy-model")

from agent.tools import python_exec, git_status, web_search


def test_git_status():
    out = git_status.run({})
    assert isinstance(out, str)


def test_python_exec_timeout():
    res = python_exec.run({"code": "print('hi')"})
    assert "hi" in res


def test_web_search():
    res = web_search.run({"query": "OpenAI"})
    assert isinstance(res, str)
