from __future__ import annotations

import ctypes
import platform
from pathlib import Path
from typing import Optional


class NativeStats(ctypes.Structure):
    _fields_ = [
        ("bytes", ctypes.c_uint64),
        ("lines", ctypes.c_uint64),
        ("characters", ctypes.c_uint64),
    ]


def _candidate_paths() -> list[Path]:
    project_root = Path(__file__).resolve().parents[2]
    build = project_root / "build"
    system = platform.system()
    names = {
        "Windows": ["wordscope_native.dll", "libwordscope_native.dll"],
        "Darwin": ["libwordscope_native.dylib"],
    }.get(system, ["libwordscope_native.so"])
    return [build / name for name in names]


class NativeEngine:
    def __init__(self) -> None:
        self._library = None
        for path in _candidate_paths():
            if path.is_file():
                try:
                    lib = ctypes.CDLL(str(path))
                    fn = lib.wordscope_measure
                    fn.argtypes = [
                        ctypes.c_char_p,
                        ctypes.c_uint64,
                        ctypes.POINTER(ctypes.c_uint64),
                        ctypes.POINTER(ctypes.c_uint64),
                        ctypes.POINTER(ctypes.c_uint64),
                    ]
                    fn.restype = None
                    self._library = lib
                    self._measure = fn
                    break
                except (OSError, AttributeError):
                    continue

    @property
    def available(self) -> bool:
        return self._library is not None

    def measure(self, data: bytes) -> Optional[dict[str, int]]:
        if not self.available:
            return None
        byte_count = ctypes.c_uint64()
        line_count = ctypes.c_uint64()
        char_count = ctypes.c_uint64()
        buffer = ctypes.create_string_buffer(data)
        self._measure(
            ctypes.cast(buffer, ctypes.c_char_p),
            len(data),
            ctypes.byref(byte_count),
            ctypes.byref(line_count),
            ctypes.byref(char_count),
        )
        return {
            "bytes": byte_count.value,
            "lines": line_count.value,
            "characters": char_count.value,
        }
