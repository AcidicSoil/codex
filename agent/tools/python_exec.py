import subprocess
import textwrap
import tempfile
from agent.config import settings

SCHEMA = {
    "name": "python_exec",
    "description": "Run short Python snippets in a sandboxed Docker container",
    "parameters": {
        "type": "object",
        "properties": {
            "code": {"type": "string", "description": "Python code"},
        },
        "required": ["code"],
    },
}

def run(args: dict) -> str:
    code = textwrap.dedent(args["code"])
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tf:
        tf.write(code)
        tf.flush()
        cmd = [
            "docker", "run", "--rm",
            "--network", "none",
            "--memory", "256m",
            "-v", f"{tf.name}:/tmp/code.py:ro",
            "python:3.12-alpine",
            "python", "/tmp/code.py",
        ]
        try:
            out = subprocess.check_output(cmd, text=True, timeout=settings.py_timeout)
            return out[:4000]
        except subprocess.CalledProcessError as e:
            return f"ERROR: {e.stdout}{e.stderr}"
        except subprocess.TimeoutExpired:
            return "ERROR: execution timed-out"
