import os
from pydantic import BaseModel, Field

class Settings(BaseModel):
    api_base: str = Field(default_factory=lambda: os.environ.get("OPENAI_API_BASE", ""))
    api_key: str = Field(default_factory=lambda: os.environ.get("OPENAI_API_KEY", ""))
    model: str = Field(default_factory=lambda: os.environ.get("MODEL_NAME", ""))
    max_iter: int = Field(default_factory=lambda: int(os.environ.get("MAX_ITERATIONS", 6)))
    debug: bool = Field(default_factory=lambda: os.environ.get("DEBUG", "0") == "1")
    py_timeout: int = Field(default_factory=lambda: int(os.environ.get("PY_EXEC_TIMEOUT", 15)))
    allowed_cmds: str = Field(default_factory=lambda: os.environ.get("ALLOWED_SHELL_CMDS", "git status,ls,cat"))

    @property
    def allowed_list(self) -> set[str]:
        return {c.strip() for c in self.allowed_cmds.split(',')}

settings = Settings()
