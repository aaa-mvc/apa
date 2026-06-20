"""workspace 历史记录管理。"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class HistoryEntry:
    ts: str
    action: str          # "generate" | "edit"
    prompt: str
    out: str
    url: str | None
    preset: str | None
    size: str
    quality: str
    fmt: str
    background: str | None
    parent: str | None   # edit 时所用上一张图
    mask: str | None
    usage: dict
    elapsed_sec: float
    revised_prompt: str = ""
    note: str = ""


def workspace_dir(base: str | Path = "workspace") -> Path:
    p = Path(base).expanduser().resolve()
    p.mkdir(parents=True, exist_ok=True)
    return p


def history_path(base: str | Path = "workspace") -> Path:
    return workspace_dir(base) / "history.jsonl"


def append_history(entry: HistoryEntry, base: str | Path = "workspace") -> None:
    p = history_path(base)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")


def read_history(base: str | Path = "workspace") -> list[dict[str, Any]]:
    p = history_path(base)
    if not p.exists():
        return []
    out: list[dict] = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def latest_for(path: str, base: str | Path = "workspace") -> dict | None:
    """找历史里产出某个文件路径的最后一条记录。"""
    target = str(Path(path).expanduser().resolve())
    last = None
    for e in read_history(base):
        if e.get("out"):
            try:
                if Path(e["out"]).expanduser().resolve() == Path(target):
                    last = e
            except Exception:
                if e["out"] == path:
                    last = e
    return last


def make_ts() -> str:
    return time.strftime("%Y%m%d_%H%M%S")
