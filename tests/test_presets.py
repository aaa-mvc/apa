"""测试 presets.py — 预设加载与尺寸解析。"""

import os
import sys
from pathlib import Path

# 把 lib/ 加到 path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.presets import get_preset, load_presets, resolve_size


class TestLoadPresets:
    def test_load_returns_dict(self):
        data = load_presets()
        assert "presets" in data
        assert "ratio_alias" in data

    def test_all_preset_sizes_are_valid(self):
        """预设尺寸必须属于 gpt-image-2 支持的四个值。"""
        VALID_SIZES = {"1024x1024", "1024x1536", "1536x1024", "auto"}
        data = load_presets()
        for name, preset in data["presets"].items():
            size = preset["size"]
            assert size in VALID_SIZES, (
                f"预设 {name} 的 size={size} 不在 API 支持列表中 {VALID_SIZES}"
            )

    def test_known_presets_exist(self):
        for name in ["ppt_cover_169", "avatar_1k", "wechat_square", "mobile_916"]:
            assert get_preset(name) is not None, f"预设 {name} 不存在"


class TestResolveSize:
    def test_preset_overrides_size(self):
        """--preset 优先于 --size。"""
        size, preset_dict = resolve_size(size="16:9", preset="avatar_1k")
        assert size == "1024x1024"  # avatar_1k 的尺寸
        assert preset_dict is not None
        assert preset_dict["label"] == "头像 1024"

    def test_size_alias_resolution(self):
        """比例别名解析。"""
        size, preset_dict = resolve_size(size="1:1", preset=None)
        assert size == "1024x1024"
        assert preset_dict is None

    def test_direct_pixel_size(self):
        """直接传 WxH 尺寸。"""
        size, preset_dict = resolve_size(size="1024x1536", preset=None)
        assert size == "1024x1536"
        assert preset_dict is None

    def test_default_when_both_omitted(self):
        """都不传时默认 1024x1024。"""
        size, preset_dict = resolve_size(size=None, preset=None)
        assert size == "1024x1024"
        assert preset_dict is None

    def test_unknown_preset_raises(self):
        """未知预设名抛出异常。"""
        try:
            resolve_size(size=None, preset="nonexistent_preset_xyz")
            assert False, "应该抛出 ValueError"
        except ValueError:
            pass

    def test_invalid_size_string_raises(self):
        """无法解析的 size 字符串抛出异常。"""
        try:
            resolve_size(size="not_a_size", preset=None)
            assert False, "应该抛出 ValueError"
        except ValueError:
            pass
