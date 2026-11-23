"""Text file loading helpers."""

from pathlib import Path


def load_text(path: Path, encoding: str = "utf-8") -> str:
    """Read a text file, replacing invalid byte sequences instead of failing."""
    return path.read_text(encoding=encoding, errors="replace")


def is_probably_text(path: Path, sample_size: int = 4096) -> bool:
    """Return False for files that appear to contain binary data."""
    try:
        sample = path.read_bytes()[:sample_size]
    except OSError:
        return False

    if b"\\x00" in sample:
        return False

    if not sample:
        return True

    # Treat a file as text when most bytes are printable or whitespace.
    allowed_controls = {9, 10, 12, 13}
    printable = sum(
        byte >= 32 or byte in allowed_controls
        for byte in sample
    )
    return printable / len(sample) >= 0.85
