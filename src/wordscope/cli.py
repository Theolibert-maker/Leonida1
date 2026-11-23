from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .native import NativeEngine
from .report import render_text
from services.scan_service import scan_path
from services.export_service import export_json
from utils.validators import validate_top_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wordscope",
        description="Анализатор текстовых файлов на Python и C++.",
    )
    parser.add_argument("path", type=Path, help="Файл или каталог")
    parser.add_argument("-r", "--recursive", action="store_true", help="Обходить подкаталоги")
    parser.add_argument("--json", type=Path, metavar="FILE", help="Сохранить JSON-отчёт")
    parser.add_argument("--top", type=int, default=8, help="Сколько частых слов показывать")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        validate_top_count(args.top)
        engine = NativeEngine()
        results = scan_path(args.path, args.recursive, engine)
        for result in results:
            result["top_words"] = result["top_words"][:args.top]

        print(render_text(results))
        if args.json:
            destination = export_json(results, args.json)
            print(f"\nJSON-отчёт сохранён: {destination}")
        if not engine.available:
            print("\nПодсказка: соберите C++-модуль через CMake для нативных метрик.")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
