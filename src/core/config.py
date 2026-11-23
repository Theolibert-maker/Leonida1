"""Application configuration and path handling."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """Runtime options shared by the CLI and services."""

    encoding: str = "utf-8"
    max_sample_bytes: int = 4096
    default_top_words: int = 8

    @staticmethod
    def normalize_path(value: str | Path) -> Path:
        return Path(value).expanduser().resolve()
