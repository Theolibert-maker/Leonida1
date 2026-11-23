from __future__ import annotations

import json
from pathlib import Path
from typing import Sequence


def totals(results: Sequence[dict]) -> dict[str, int]:
    keys = ("bytes", "lines", "characters", "words")
    return {key: sum(item[key] for item in results) for key in keys}


def render_text(results: Sequence[dict]) -> str:
    if not results:
        return "Подходящие файлы не найдены."

    rows = []
    for item in results:
        rows.append(
            f"{item['path']}\n"
            f"  строк: {item['lines']} | слов: {item['words']} | "
            f"символов: {item['characters']} | байт: {item['bytes']} "
            f"| движок: {item['engine']}"
        )
        common = ", ".join(f"{word} ({count})" for word, count in item["top_words"][:8])
        if common:
            rows.append(f"  частые слова: {common}")

    summary = totals(results)
    rows.append(
        "\nИТОГО: "
        + " | ".join(f"{key}: {value}" for key, value in summary.items())
    )
    return "\n".join(rows)


def write_json(results: Sequence[dict], destination: Path) -> None:
    payload = {"files": list(results), "totals": totals(results)}
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
