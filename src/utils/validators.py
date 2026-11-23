"""Input validation helpers."""

from pathlib import Path


def validate_input_path(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    if not resolved.exists():
        raise FileNotFoundError(f"Input path does not exist: {resolved}")
    if not (resolved.is_file() or resolved.is_dir()):
        raise ValueError(f"Input path is not a file or directory: {resolved}")
    return resolved


def validate_top_count(value: int) -> int:
    if value < 0:
        raise ValueError("--top must be zero or greater")
    return value
