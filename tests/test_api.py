"""测试 api.py — 尺寸归一化与客户端逻辑（不触发真实 API 调用）。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.api import GPTImageClient


class TestNormalizeSize:
    def setup_method(self):
        # 使用 mock 凭据创建客户端（不实际调用 API）
        self.client = GPTImageClient(
            base_url="http://localhost:9999/v1",
            api_key="test-key",
            model="gpt-image-2",
        )

    def test_supported_sizes_pass_through(self):
        """API 原生支持的尺寸直接通过。"""
        for size in ["1024x1024", "1024x1536", "1536x1024", "auto"]:
            assert self.client._normalize_size(size) == size

    def test_near_square_normalizes_correctly(self):
        """接近 1:1 的尺寸归一为 1024x1024。"""
        assert self.client._normalize_size("800x800") == "1024x1024"
        assert self.client._normalize_size("900x600") == "1024x1024"

    def test_wide_normalizes_to_1536x1024(self):
        """宽幅尺寸归一为 1536x1024。"""
        assert self.client._normalize_size("1920x1080") == "1536x1024"
        assert self.client._normalize_size("1600x900") == "1536x1024"

    def test_tall_normalizes_to_1024x1536(self):
        """竖幅尺寸归一为 1024x1536。"""
        assert self.client._normalize_size("1080x1920") == "1024x1536"
        assert self.client._normalize_size("750x1334") == "1024x1536"

    def test_default(self):
        """空值默认 1024x1024。"""
        assert self.client._normalize_size("") == "1024x1024"
        assert self.client._normalize_size(None) == "1024x1024"

    def test_case_insensitive(self):
        assert self.client._normalize_size("AUTO") == "auto"

    def test_invalid_raises(self):
        try:
            self.client._normalize_size("not_a_valid_size_spec")
            assert False, "应该抛出 ValueError"
        except ValueError:
            pass
