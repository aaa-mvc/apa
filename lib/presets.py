"""办公场景预设加载 & 尺寸/比例解析。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_PRESETS_PATH = Path(__file__).resolve().parent.parent / "presets" / "presets.json"


def load_presets() -> dict[str, Any]:
    """加载预设表（懒加载并缓存）。"""
    if not _PRESETS_PATH.exists():
        return {"presets": {}, "ratio_alias": {}}
    return json.loads(_PRESETS_PATH.read_text(encoding="utf-8"))


def get_preset(name: str) -> dict | None:
    """按预设名查找。"""
    return load_presets().get("presets", {}).get(name)


def resolve_size(size: str | None, preset: str | None) -> tuple[str, dict | None]:
    """把 --size / --preset 解析成 (size, preset_dict)。

    返回 size 是 gpt-image-2 支持的字符串（如 1024x1024）。
    """
    if preset:
        p = get_preset(preset)
        if not p:
            raise ValueError(f"未知预设: {preset}。可用预设：{list(load_presets().get('presets', {}).keys())}")
        return p["size"], p
    if not size:
        return "1024x1024", None
    s = size.strip().lower()
    if "x" in s:
        return s, None
    alias = load_presets().get("ratio_alias", {})
    if s in alias:
        return alias[s], None
    raise ValueError(f"无法解析 size: {size}（支持 WxH / 1:1 / 16:9 / auto / 预设名）")
