from __future__ import annotations

import ctypes
import hashlib
import platform
from pathlib import Path
from typing import Optional


def _candidate_paths() -> list[Path]:
    project_root = Path(__file__).resolve().parents[2]
    build = project_root / "build"
    names = {
        "Windows": ["wordscope_native.dll", "libwordscope_native.dll"],
        "Darwin": ["libwordscope_native.dylib"],
    }.get(platform.system(), ["libwordscope_native.so"])
    return [build / name for name in names]


class NativeEngine:
    def __init__(self) -> None:
        self._library = None
        for path in _candidate_paths():
            if not path.is_file():
                continue
            try:
                lib = ctypes.CDLL(str(path))
                lib.wordscope_measure.argtypes = [
                    ctypes.c_char_p, ctypes.c_uint64,
                    ctypes.POINTER(ctypes.c_uint64),
                    ctypes.POINTER(ctypes.c_uint64),
                    ctypes.POINTER(ctypes.c_uint64),
                ]
                lib.wordscope_measure.restype = None
                lib.wordscope_hash.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
                lib.wordscope_hash.restype = ctypes.c_uint64
                lib.wordscope_valid_utf8.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
                lib.wordscope_valid_utf8.restype = ctypes.c_int
                self._library = lib
                break
            except (OSError, AttributeError):
                continue

    @property
    def available(self) -> bool:
        return self._library is not None

    def measure(self, data: bytes) -> Optional[dict[str, int | str | bool]]:
        if not self.available:
            return None
        byte_count, line_count, char_count = (ctypes.c_uint64() for _ in range(3))
        buffer = ctypes.create_string_buffer(data)
        pointer = ctypes.cast(buffer, ctypes.c_char_p)
        size = len(data)
        self._library.wordscope_measure(
            pointer, size, ctypes.byref(byte_count),
            ctypes.byref(line_count), ctypes.byref(char_count),
        )
        fingerprint = self._library.wordscope_hash(pointer, size)
        valid_utf8 = bool(self._library.wordscope_valid_utf8(pointer, size))
        return {
            "bytes": byte_count.value,
            "lines": line_count.value,
            "characters": char_count.value,
            "fingerprint": f"{fingerprint:016x}",
            "valid_utf8": valid_utf8,
        }

    @staticmethod
    def fallback_fingerprint(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()[:16]
