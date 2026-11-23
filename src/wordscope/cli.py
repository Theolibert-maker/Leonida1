from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .analyzer import analyze_file, discover_files
from .native import NativeEngine
from .report import render_text, write_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wordscope",
        description="Анализатор текстовых файлов на Python и C++.",
    )
    parser.add_argument("path", type=Path, help="Файл или каталог")
    parser.add_argument("-r", "--recursive", action="store_true", help="Обходить подкаталоги")
    parser.add_argument("--json", type=Path, metavar="FILE", help="Сохранить JSON-отчёт")
    parser.add_argument("--top", type=int, default=8, help="Сколько частых слов показывать (по умолчанию: 8)")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.top < 0:
        print("--top не может быть отрицательным", file=sys.stderr)
        return 2

    try:
        engine = NativeEngine()
        files = list(discover_files(args.path, args.recursive))
        results = [analyze_file(path, engine) for path in files]
        for result in results:
            result["top_words"] = result["top_words"][:args.top]

        print(render_text(results))
        if args.json:
            write_json(results, args.json)
            print(f"\nJSON-отчёт сохранён: {args.json}")
        if not engine.available:
            print("\nПодсказка: соберите C++-модуль через CMake для нативного подсчёта метрик.")
        return 0
    except (OSError, UnicodeError, FileNotFoundError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1
