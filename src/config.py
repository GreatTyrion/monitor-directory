from pathlib import Path

from pydantic import BaseSettings

WATCH_DIRECTORY = str(Path.cwd() / "downloads")


class Settings(BaseSettings):
    watch_directory: str = WATCH_DIRECTORY
    watch_delay: int = 5
    watch_recursively: bool = True
    watch_pattern: str = "*"


settings = Settings()