"""Filesystem helpers shared by scan and export services."""

from pathlib import Path
from typing import Iterator


TEXT_EXTENSIONS = {
    ".txt", ".md", ".rst", ".log", ".csv", ".json", ".xml",
    ".yaml", ".yml", ".toml", ".ini", ".py", ".cpp", ".h", ".hpp",
}


def iter_files(target: Path, recursive: bool = False) -> Iterator[Path]:
    if target.is_file():
        yield target
        return
    if not target.is_dir():
        raise FileNotFoundError(f"Path does not exist: {target}")

    entries = target.rglob("*") if recursive else target.iterdir()
    for entry in sorted(entries):
        if entry.is_file():
            yield entry


def has_text_extension(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS
