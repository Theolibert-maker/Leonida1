from wordscope.analyzer import analyze_text, discover_files


class PythonOnlyEngine:
    def measure(self, data):
        return None


def test_unicode_metrics_and_words():
    result = analyze_text("Hello, мир!\nHello world.", PythonOnlyEngine())
    assert result["lines"] == 2
    assert result["words"] == 4
    assert result["unique_words"] == 3
    assert result["top_words"][0] == ("hello", 2)
    assert result["engine"] == "Python"


def test_discover_single_file(tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text("abc", encoding="utf-8")
    assert list(discover_files(sample)) == [sample]


def test_discover_directory_recursive(tmp_path):
    (tmp_path / "a.txt").write_text("a", encoding="utf-8")
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "b.txt").write_text("b", encoding="utf-8")
    assert len(list(discover_files(tmp_path, recursive=True))) == 2
