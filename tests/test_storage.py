"""测试 storage.py — 历史记录与 workspace 管理。"""

import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.storage import (
    HistoryEntry,
    append_history,
    make_ts,
    read_history,
    workspace_dir,
)


class TestMakeTs:
    def test_returns_non_empty_string(self):
        ts = make_ts()
        assert len(ts) > 0

    def test_format_is_yyyymmdd_hhmmss(self):
        ts = make_ts()
        # 格式: 20260619_093045
        parts = ts.split("_")
        assert len(parts) == 2
        assert len(parts[0]) == 8  # YYYYMMDD
        assert len(parts[1]) == 6  # HHMMSS


class TestWorkspaceDir:
    def test_creates_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = workspace_dir(tmp)
            assert ws.is_dir()

    def test_returns_absolute_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = workspace_dir(tmp)
            assert ws.is_absolute()


class TestHistory:
    def test_append_and_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            entry = HistoryEntry(
                ts="20260619_120000",
                action="generate",
                prompt="a red apple",
                out=f"{tmp}/test.png",
                url="https://example.com/img.png",
                preset="avatar_1k",
                size="1024x1024",
                quality="standard",
                fmt="png",
                background=None,
                parent=None,
                mask=None,
                usage={"total_tokens": 100},
                elapsed_sec=10.5,
                revised_prompt="",
                note="",
            )
            append_history(entry, base=tmp)
            records = read_history(base=tmp)
            assert len(records) == 1
            r = records[0]
            assert r["action"] == "generate"
            assert r["prompt"] == "a red apple"
            assert r["preset"] == "avatar_1k"
            assert r["usage"]["total_tokens"] == 100
            assert r["elapsed_sec"] == 10.5

    def test_read_empty_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            records = read_history(base=tmp)
            assert records == []

    def test_append_multiple(self):
        with tempfile.TemporaryDirectory() as tmp:
            for i in range(5):
                append_history(
                    HistoryEntry(
                        ts=f"20260619_{i:06d}",
                        action="generate",
                        prompt=f"test {i}",
                        out=f"{tmp}/test_{i}.png",
                        url=None,
                        preset=None,
                        size="1024x1024",
                        quality="standard",
                        fmt="png",
                        background=None,
                        parent=None,
                        mask=None,
                        usage={},
                        elapsed_sec=1.0,
                    ),
                    base=tmp,
                )
            records = read_history(base=tmp)
            assert len(records) == 5

    def test_read_history_respects_order(self):
        """读取顺序与写入顺序一致。"""
        with tempfile.TemporaryDirectory() as tmp:
            for i in range(3):
                append_history(
                    HistoryEntry(
                        ts=f"20260619_00000{i}",
                        action="generate",
                        prompt=f"test {i}",
                        out=f"{tmp}/test_{i}.png",
                        url=None,
                        preset=None,
                        size="1024x1024",
                        quality="standard",
                        fmt="png",
                        background=None,
                        parent=None,
                        mask=None,
                        usage={},
                        elapsed_sec=1.0,
                    ),
                    base=tmp,
                )
            records = read_history(base=tmp)
            prompts = [r["prompt"] for r in records]
            assert prompts == ["test 0", "test 1", "test 2"]
