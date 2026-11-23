from pathlib import Path

from utils.validators import validate_top_count
from utils.file_utils import has_text_extension


def test_top_count_validation():
    assert validate_top_count(0) == 0


def test_reject_negative_top_count():
    try:
        validate_top_count(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative count should be rejected")


def test_text_extension_filter():
    assert has_text_extension(Path("notes.md"))
    assert not has_text_extension(Path("picture.png"))
