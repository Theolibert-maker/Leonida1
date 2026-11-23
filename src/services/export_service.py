"""Report export workflows."""

from pathlib import Path
from typing import Sequence

from wordscope.report import write_json


def export_json(results: Sequence[dict], destination: Path) -> Path:
    destination = destination.expanduser()
    write_json(results, destination)
    return destination.resolve()
