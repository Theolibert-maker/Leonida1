from __future__ import annotations

from collections import Counter
import hashlib
from pathlib import Path
import re
from typing import Iterable

from .native import NativeEngine
from .text_loader import load_text
from utils.file_utils import iter_files

_WORD_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)?", re.UNICODE)


def _python_metrics(text: str) -> dict[str, int]:
    lines = text.count("\n")
    if text and not text.endswith("\n"):
        lines += 1
    return {
        "bytes": len(text.encode("utf-8")),
        "lines": lines,
        "characters": len(text),
    }


def analyze_text(text: str, engine: NativeEngine | None = None) -> dict:
    engine = engine or NativeEngine()
    encoded = text.encode("utf-8")
    native_metrics = engine.measure(encoded)
    metrics = native_metrics or _python_metrics(text)
    metrics.setdefault("fingerprint", hashlib.sha256(encoded).hexdigest()[:16])
    metrics.setdefault("valid_utf8", True)

    # Python owns Unicode tokenization and frequency analysis.
    words = [match.group(0).casefold() for match in _WORD_RE.finditer(text)]
    frequencies = Counter(words)

    return {
        **metrics,
        "words": len(words),
        "unique_words": len(frequencies),
        "top_words": frequencies.most_common(20),
        "engine": "C++" if native_metrics is not None else "Python",
    }


def analyze_file(path: Path, engine: NativeEngine | None = None) -> dict:
    text = load_text(path)
    return {"path": str(path), **analyze_text(text, engine)}


def discover_files(target: Path, recursive: bool = False) -> Iterable[Path]:
    yield from iter_files(target, recursive)
