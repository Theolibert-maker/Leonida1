"""Coordinates discovery and analysis of multiple files."""

from pathlib import Path

from wordscope.analyzer import analyze_file
from wordscope.native import NativeEngine
from utils.file_utils import iter_files, has_text_extension
from utils.validators import validate_input_path
from core.logger import get_logger


logger = get_logger(__name__)


def scan_path(
    target: Path,
    recursive: bool = False,
    engine: NativeEngine | None = None,
) -> list[dict]:
    target = validate_input_path(target)
    engine = engine or NativeEngine()
    results = []
    for path in iter_files(target, recursive=recursive):
        if target.is_dir() and not has_text_extension(path):
            logger.debug("Skipping unsupported extension: %s", path)
            continue
        results.append(analyze_file(path, engine))
    return results
