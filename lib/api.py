"""gpt-image-2 图像生成 API 客户端（OpenAI 兼容协议）。

支持：
  - 文生图（images/generations）
  - 以图生图（images/edits，单图/多图/带蒙版）
"""

from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    from dotenv import load_dotenv
    # 优先加载 skill 根目录下的 .env；不强制要求存在（未安装 dotenv 时降级为只读环境变量）
    _env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(_env_path, override=False)
except ImportError:
    pass


def _env(name: str, default: str | None = None) -> str:
    val = os.environ.get(name, default)
    if val is None:
        raise EnvironmentError(
            f"环境变量 {name} 未设置。\n"
            f"  export {name}=...   # 写入 ~/.zshrc 持久化\n"
            f"  或在 skill 根目录的 .env 中配置 {name}=..."
        )
    return val


@dataclass
class GenResult:
    """一次生图结果。"""

    images: list[dict]   # [{"path": ..., "url": ..., "b64": ...}, ...]
    revised_prompt: str
    usage: dict
    raw: dict
    elapsed_sec: float

    def first_path(self) -> str:
        return self.images[0]["path"] if self.images else ""


class APIError(RuntimeError):
    def __init__(self, status: int, body: str):
        super().__init__(f"HTTP {status}: {body[:500]}")
        self.status = status
        self.body = body


class GPTImageClient:
    """gpt-image-2 客户端。"""

    SUPPORTED_SIZES = {"1024x1024", "1024x1536", "1536x1024", "auto"}

    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        model: str | None = None,
        timeout: int = 300,
    ):
        self.base_url = (base_url or _env("AI_API_BASE_URL")).rstrip("/")
        self.api_key = api_key or _env("AI_API_KEY")
        self.model = model or _env("AI_MODEL", "gpt-image-2")
        self.timeout = timeout

    # ---- HTTP --------------------------------------------------------

    def _request_json(self, method: str, path: str, payload: dict) -> dict:
        # path 通常以 /v1/... 开头；若 base_url 已带 /v1，则去重
        url_path = path
        if self.base_url.endswith("/v1") and path.startswith("/v1"):
            url_path = path[len("/v1"):]
        url = f"{self.base_url}{url_path}"
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            raise APIError(e.code, body) from None
        except urllib.error.URLError as e:
            raise APIError(0, f"网络错误: {e}") from None

    def _request_multipart(
        self,
        path: str,
        fields: dict,
        files: list[tuple[str, str, bytes, str]],
    ) -> dict:
        """简易 multipart/form-data 提交。files = [(field_name, filename, data, content_type), ...]"""
        import uuid
        import mimetypes

        boundary = "----GPTIMG" + uuid.uuid4().hex
        chunks: list[bytes] = []
        for k, v in fields.items():
            chunks.append(f"--{boundary}\r\n".encode())
            chunks.append(
                f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode()
            )
            chunks.append(str(v).encode("utf-8"))
            chunks.append(b"\r\n")
        for field_name, filename, data, ctype in files:
            chunks.append(f"--{boundary}\r\n".encode())
            chunks.append(
                f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'.encode()
            )
            ctype = ctype or (mimetypes.guess_type(filename)[0] or "application/octet-stream")
            chunks.append(f"Content-Type: {ctype}\r\n\r\n".encode())
            chunks.append(data)
            chunks.append(b"\r\n")
        chunks.append(f"--{boundary}--\r\n".encode())

        body = b"".join(chunks)
        url_path = path
        if self.base_url.endswith("/v1") and path.startswith("/v1"):
            url_path = path[len("/v1"):]
        url = f"{self.base_url}{url_path}"
        req = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Content-Length": str(len(body)),
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise APIError(e.code, err_body) from None
        except urllib.error.URLError as e:
            raise APIError(0, f"网络错误: {e}") from None

    # ---- 高层 API ---------------------------------------------------

    def _normalize_size(self, size: str) -> str:
        size = (size or "1024x1024").strip().lower()
        if size == "auto":
            return "auto"
        if size in self.SUPPORTED_SIZES:
            return size
        # 解析 WxH
        if "x" in size:
            w, h = size.split("x", 1)
            wn, hn = int(w), int(h)
            # 模型仅支持 1024 一档；对其它尺寸做最接近的归一化提示
            mapping = {
                (1024, 1024): "1024x1024",
                (1024, 1536): "1024x1536",
                (1536, 1024): "1536x1024",
            }
            closest = min(
                mapping.keys(),
                key=lambda k: abs(k[0] - wn) / max(k[0], 1) + abs(k[1] - hn) / max(k[1], 1),
            )
            chosen = mapping[closest]
            print(
                f"  ℹ️  尺寸 {size} 不在 gpt-image-2 支持列表，已就近归一为 {chosen}",
                file=sys.stderr,
            )
            return chosen
        raise ValueError(
            f"无法解析 size: {size}。支持: {sorted(self.SUPPORTED_SIZES)} 或 WxH"
        )

    def _save_image(
        self,
        item: dict,
        out_dir: Path,
        ts: str,
        idx: int,
        fmt_hint: str,
    ) -> dict:
        """从响应项保存一张图片到磁盘，返回 {path, url, b64}。"""
        out_dir.mkdir(parents=True, exist_ok=True)
        ext = fmt_hint if fmt_hint in ("png", "jpg", "webp") else "png"
        if fmt_hint == "jpg":
            ext = "jpg"
        filename = f"{ts}_{idx:02d}.{ext}"
        path = out_dir / filename

        if "b64_json" in item and item["b64_json"]:
            data = base64.b64decode(item["b64_json"])
            path.write_bytes(data)
            return {"path": str(path), "url": None, "b64": item["b64_json"]}
        if "url" in item and item["url"]:
            # 下载到本地（同时保留 URL）
            try:
                req = urllib.request.Request(item["url"], method="GET")
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = resp.read()
                path.write_bytes(data)
            except Exception as e:
                print(f"  ⚠️  下载图片失败: {e}，仅保留远程 URL", file=sys.stderr)
            return {"path": str(path), "url": item["url"], "b64": None}
        raise APIError(0, "响应中没有 b64_json 或 url 字段")

    def generate(
        self,
        prompt: str,
        *,
        size: str = "1024x1024",
        n: int = 1,
        quality: str = "standard",
        fmt: str = "png",
        background: str | None = None,
        out_dir: str | Path = "workspace",
    ) -> GenResult:
        """文生图。返回 GenResult。"""
        if not prompt or not prompt.strip():
            raise ValueError("prompt 不能为空")

        size = self._normalize_size(size)
        payload: dict = {
            "model": self.model,
            "prompt": prompt,
            "n": n,
            "size": size,
            "quality": quality,
            "response_format": "url",
        }
        if background:
            payload["background"] = background

        t0 = time.time()
        resp = self._request_json("POST", "/v1/images/generations", payload)
        elapsed = time.time() - t0

        ts = time.strftime("%Y%m%d_%H%M%S")
        images = [
            self._save_image(item, Path(out_dir), ts, i, fmt)
            for i, item in enumerate(resp.get("data", []), 1)
        ]
        revised = ""
        if images and resp.get("data"):
            revised = resp["data"][0].get("revised_prompt", "") or ""

        return GenResult(
            images=images,
            revised_prompt=revised,
            usage=resp.get("usage", {}),
            raw=resp,
            elapsed_sec=elapsed,
        )

    def edit(
        self,
        image_paths: Iterable[str | Path],
        prompt: str,
        *,
        mask_path: str | Path | None = None,
        size: str | None = None,
        n: int = 1,
        quality: str = "standard",
        fmt: str | None = None,
        out_dir: str | Path = "workspace",
    ) -> GenResult:
        """以图生图 / 蒙版编辑。

        image_paths: 一张或多张参考图
        mask_path: 可选蒙版（PNG，白色=编辑区）
        size: 可选；不传则跟随输入图
        """
        image_paths = [Path(p) for p in image_paths]
        if not image_paths:
            raise ValueError("至少需要一张输入图")
        for p in image_paths:
            if not p.exists():
                raise FileNotFoundError(f"输入图不存在: {p}")

        if mask_path is not None:
            mask_path = Path(mask_path)
            if not mask_path.exists():
                raise FileNotFoundError(f"蒙版不存在: {mask_path}")

        if not prompt or not prompt.strip():
            raise ValueError("prompt 不能为空")

        fields: dict = {
            "model": self.model,
            "prompt": prompt,
            "n": str(n),
            "response_format": "url",
        }
        if size:
            fields["size"] = self._normalize_size(size)
        if quality:
            fields["quality"] = quality

        files: list[tuple[str, str, bytes, str]] = []
        for p in image_paths:
            # 多图用 "image[]"（PHP-style multipart array），单图用 "image"
            field = "image[]" if len(image_paths) > 1 else "image"
            data = p.read_bytes()
            ctype = "image/png"
            if p.suffix.lower() in (".jpg", ".jpeg"):
                ctype = "image/jpeg"
            elif p.suffix.lower() == ".webp":
                ctype = "image/webp"
            files.append((field, p.name, data, ctype))
        if mask_path is not None:
            files.append(
                ("mask", mask_path.name, mask_path.read_bytes(), "image/png")
            )

        t0 = time.time()
        resp = self._request_multipart(
            "/v1/images/edits", fields=fields, files=files
        )
        elapsed = time.time() - t0

        ts = time.strftime("%Y%m%d_%H%M%S")
        # 输出格式：显式 > 输入图格式 > png
        out_fmt = fmt or (image_paths[0].suffix.lstrip(".").lower() or "png")
        if out_fmt == "jpeg":
            out_fmt = "jpg"
        images = [
            self._save_image(item, Path(out_dir), ts, i, out_fmt)
            for i, item in enumerate(resp.get("data", []), 1)
        ]
        revised = ""
        if resp.get("data"):
            revised = resp["data"][0].get("revised_prompt", "") or ""

        return GenResult(
            images=images,
            revised_prompt=revised,
            usage=resp.get("usage", {}),
            raw=resp,
            elapsed_sec=elapsed,
        )
