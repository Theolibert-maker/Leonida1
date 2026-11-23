from wordscope.report import totals, write_json
import json


def test_totals():
    data = [
        {"bytes": 3, "lines": 1, "characters": 3, "words": 1},
        {"bytes": 5, "lines": 2, "characters": 5, "words": 2},
    ]
    assert totals(data) == {"bytes": 8, "lines": 3, "characters": 8, "words": 3}


def test_json_output(tmp_path):
    destination = tmp_path / "out" / "report.json"
    write_json([], destination)
    assert json.loads(destination.read_text(encoding="utf-8"))["files"] == []
