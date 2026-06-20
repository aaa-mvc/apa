#!/usr/bin/env python3
"""gpt-image-2 skill 的 CLI 入口。

子命令：
  generate   文生图
  edit       以图生图 / 蒙版编辑
  history    列出工作区历史
  preset     列出 / 查找预设
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# 允许作为脚本直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.api import APIError, GPTImageClient
from lib.presets import get_preset, load_presets, resolve_size
from lib.storage import (
    HistoryEntry,
    append_history,
    history_path,
    make_ts,
    read_history,
    workspace_dir,
)


def _print_kv(d: dict, indent: int = 0) -> None:
    pad = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{pad}{k}:")
            _print_kv(v, indent + 1)
        else:
            print(f"{pad}{k}: {v}")


def _resolve_out(out: str | None, workspace: Path, action: str, fmt: str, ts: str) -> Path:
    if out:
        p = Path(out).expanduser()
        p.parent.mkdir(parents=True, exist_ok=True)
        return p
    ts_name = f"{ts}_{action}"
    ext = fmt if fmt in ("png", "jpg", "webp") else "png"
    return workspace / f"{ts_name}.{ext}"


def cmd_generate(args: argparse.Namespace) -> int:
    size, preset = resolve_size(args.size, args.preset)
    fmt = args.format or (preset or {}).get("format", "png")
    background = args.background or (preset or {}).get("background")
    quality = args.quality

    workspace = workspace_dir(args.workspace)
    ts = make_ts()
    out_path = _resolve_out(args.out, workspace, "gen", fmt, ts)

    client = GPTImageClient()
    print(f"→ generate")
    print(f"  prompt: {args.prompt[:120]}{'...' if len(args.prompt) > 120 else ''}")
    print(f"  size:   {size}" + (f"  (preset: {args.preset})" if args.preset else ""))
    print(f"  quality:{quality}  format:{fmt}  n:{args.n}")
    if background:
        print(f"  background: {background}")
    print(f"  out:    {out_path}")

    try:
        result = client.generate(
            prompt=args.prompt,
            size=size,
            n=args.n,
            quality=quality,
            fmt=fmt,
            background=background,
            out_dir=out_path.parent,
        )
    except APIError as e:
        print(f"✗ API 错误: {e}", file=sys.stderr)
        return 2

    # 若 n>1，给每张图补 _NN；首张放到 out_path
    saved = result.images
    if saved:
        if args.n > 1 or len(saved) > 1:
            # 把 saved[0] 移动/重命名为 out_path
            first = Path(saved[0]["path"])
            if first != out_path:
                first.rename(out_path)
                saved[0] = {**saved[0], "path": str(out_path)}
            # 后续图直接保留
            for i, img in enumerate(saved[1:], 2):
                print(f"  ✓ saved #{i}: {img['path']}")
        else:
            first = Path(saved[0]["path"])
            if first != out_path:
                first.rename(out_path)
                saved[0] = {**saved[0], "path": str(out_path)}

    print(f"✓ done in {result.elapsed_sec:.1f}s, tokens={result.usage.get('total_tokens', '?')}")
    if saved:
        print(f"  → {saved[0]['path']}")
        if saved[0].get("url"):
            print(f"  ↗ {saved[0]['url']}")
    if result.revised_prompt:
        print(f"  revised_prompt: {result.revised_prompt[:200]}")

    # 记录历史
    append_history(
        HistoryEntry(
            ts=ts,
            action="generate",
            prompt=args.prompt,
            out=str(out_path) if saved else "",
            url=(saved[0].get("url") if saved else None),
            preset=args.preset,
            size=size,
            quality=quality,
            fmt=fmt,
            background=background,
            parent=None,
            mask=None,
            usage=result.usage,
            elapsed_sec=result.elapsed_sec,
            revised_prompt=result.revised_prompt,
        ),
        base=args.workspace,
    )
    return 0


def cmd_edit(args: argparse.Namespace) -> int:
    workspace = workspace_dir(args.workspace)
    ts = make_ts()
    size, preset = resolve_size(args.size, args.preset)
    fmt = args.format or (preset or {}).get("format")
    if fmt is None:
        # 跟输入图
        first = Path(args.image[0])
        ext = first.suffix.lstrip(".").lower()
        fmt = "jpg" if ext == "jpeg" else (ext or "png")
    out_path = _resolve_out(args.out, workspace, "edit", fmt, ts)

    client = GPTImageClient()
    print(f"→ edit")
    print(f"  prompt: {args.prompt[:120]}{'...' if len(args.prompt) > 120 else ''}")
    print(f"  image:  {args.image}" + (f"\n  mask:   {args.mask}" if args.mask else ""))
    print(f"  size:   {size}" + (f"  (preset: {args.preset})" if args.preset else ""))
    print(f"  format: {fmt}  quality: {args.quality}  n: {args.n}")
    print(f"  out:    {out_path}")

    try:
        result = client.edit(
            image_paths=args.image,
            prompt=args.prompt,
            mask_path=args.mask,
            size=size,
            n=args.n,
            quality=args.quality,
            fmt=fmt,
            out_dir=out_path.parent,
        )
    except APIError as e:
        print(f"✗ API 错误: {e}", file=sys.stderr)
        return 2

    saved = result.images
    if saved:
        first = Path(saved[0]["path"])
        if first != out_path:
            first.rename(out_path)
            saved[0] = {**saved[0], "path": str(out_path)}
        for i, img in enumerate(saved[1:], 2):
            print(f"  ✓ saved #{i}: {img['path']}")

    print(f"✓ done in {result.elapsed_sec:.1f}s, tokens={result.usage.get('total_tokens', '?')}")
    if saved:
        print(f"  → {saved[0]['path']}")
        if saved[0].get("url"):
            print(f"  ↗ {saved[0]['url']}")
    if result.revised_prompt:
        print(f"  revised_prompt: {result.revised_prompt[:200]}")

    # 记录历史：parent = 第一张输入图的绝对路径
    try:
        parent_abs = str(Path(args.image[0]).expanduser().resolve())
    except Exception:
        parent_abs = args.image[0]

    append_history(
        HistoryEntry(
            ts=ts,
            action="edit",
            prompt=args.prompt,
            out=str(out_path) if saved else "",
            url=(saved[0].get("url") if saved else None),
            preset=args.preset,
            size=size,
            quality=args.quality,
            fmt=fmt,
            background=None,
            parent=parent_abs,
            mask=(str(Path(args.mask).expanduser().resolve()) if args.mask else None),
            usage=result.usage,
            elapsed_sec=result.elapsed_sec,
            revised_prompt=result.revised_prompt,
        ),
        base=args.workspace,
    )
    return 0


def cmd_history(args: argparse.Namespace) -> int:
    entries = read_history(args.workspace)
    if args.last:
        entries = entries[-args.last:]
    if not entries:
        print("(空)")
        return 0
    for i, e in enumerate(entries, 1):
        print(
            f"[{i:3d}] {e.get('ts','')}  {e.get('action',''):8s}  "
            f"{e.get('size','')}  {e.get('preset') or '-':14s}  "
            f"{e.get('out','')}"
        )
        if args.verbose:
            prompt = e.get("prompt", "")
            if len(prompt) > 80:
                prompt = prompt[:77] + "..."
            print(f"        prompt: {prompt}")
            if e.get("parent"):
                print(f"        parent: {e['parent']}")
            if e.get("mask"):
                print(f"        mask:   {e['mask']}")
            if e.get("url"):
                print(f"        url:    {e['url']}")
            usage = e.get("usage") or {}
            if usage:
                print(f"        tokens: {usage.get('total_tokens','?')}")
    return 0


def cmd_preset(args: argparse.Namespace) -> int:
    data = load_presets()
    presets = data.get("presets", {})
    if args.name:
        p = presets.get(args.name)
        if not p:
            print(f"未知预设: {args.name}")
            print("可用：", ", ".join(sorted(presets.keys())))
            return 1
        print(f"{args.name}  ({p.get('label','')})")
        _print_kv({k: v for k, v in p.items() if k != "label"})
        return 0
    print(f"共 {len(presets)} 个预设：")
    for k in sorted(presets.keys()):
        p = presets[k]
        print(f"  {k:18s}  {p.get('size',''):12s}  {p.get('label','')}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="gpt-image",
        description="gpt-image-2 生图/改图 skill（OpenAI 兼容协议）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""示例：
  %(prog)s generate --prompt "a red apple" --size 1:1
  %(prog)s generate --prompt "PPT 封面" --preset ppt_cover_169 --format png
  %(prog)s edit --image workspace/x.png --prompt "改成夜景"
  %(prog)s edit --image a.png --mask a_mask.png --prompt "替换天空"
  %(prog)s history --last 5 --verbose
  %(prog)s preset
""",
    )
    p.add_argument(
        "--workspace",
        default="workspace",
        help="workspace 目录（保存图片和 history.jsonl）",
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    # generate
    g = sub.add_parser("generate", help="文生图")
    g.add_argument("--prompt", required=True, help="图像描述")
    g.add_argument("--size", help="WxH / 1:1 / 16:9 / auto")
    g.add_argument("--preset", help="预设名（覆盖 --size）")
    g.add_argument("--n", type=int, default=1, help="生成张数（默认 1）")
    g.add_argument("--quality", default="standard", choices=["standard", "hd"])
    g.add_argument("--format", dest="format", choices=["png", "jpg", "webp"])
    g.add_argument("--background", help="transparent 等")
    g.add_argument("--out", help="输出路径")
    g.set_defaults(func=cmd_generate)

    # edit
    e = sub.add_parser("edit", help="以图生图 / 蒙版编辑")
    e.add_argument(
        "--image",
        action="append",
        required=True,
        help="输入图（可重复多次）",
    )
    e.add_argument("--mask", help="蒙版 PNG（白=编辑区）")
    e.add_argument("--prompt", required=True)
    e.add_argument("--size", help="输出尺寸（不传则跟输入图）")
    e.add_argument("--preset", help="预设名（覆盖 --size）")
    e.add_argument("--n", type=int, default=1)
    e.add_argument("--quality", default="standard", choices=["standard", "hd"])
    e.add_argument("--format", dest="format", choices=["png", "jpg", "webp"])
    e.add_argument("--out", help="输出路径")
    e.set_defaults(func=cmd_edit)

    # history
    h = sub.add_parser("history", help="查看历史")
    h.add_argument("--last", type=int, help="只看最后 N 条")
    h.add_argument("--verbose", "-v", action="store_true")
    h.set_defaults(func=cmd_history)

    # preset
    pr = sub.add_parser("preset", help="查看预设")
    pr.add_argument("name", nargs="?", help="预设名（省略则列出全部）")
    pr.set_defaults(func=cmd_preset)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
