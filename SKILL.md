---
name: gpt-image-2
description: AI 图像生成与编辑 skill（基于 gpt-image-2）。支持文生图、以图生图、局部蒙版编辑、迭代修改。覆盖 PPT 封面、公众号头图、海报、头像、Banner、电商主图、Logo、表情包等办公场景的多比例（1:1/3:2/2:3/16:9/9:16/auto）与多格式（PNG/JPG/WebP）输出。Use when user mentions 生图, AI 画图, 生成图片, 以图生图, 编辑图片, 改图, AI 配图, 出图, 改这张图, 海报, 封面, 头像, banner, gpt-image.
---

# gpt-image-2 图像生成 Skill

基于 `gpt-image-2` 模型（OpenAI 兼容协议）的图像生成 / 编辑 / 迭代修改 skill。

**核心能力**

| 能力 | 接口 | 典型用途 |
|------|------|----------|
| 文生图 | `POST /v1/images/generations` | 从描述生成新图 |
| 以图生图 | `POST /v1/images/edits` | 基于参考图改风格/换主体/换场景 |
| 蒙版编辑 | `POST /v1/images/edits`（带 mask） | 局部重绘、抹掉水印、换背景 |
| 迭代修改 | 复用上一张图作为新输入 | "再画一版""换个颜色""改成夜晚" |

**环境配置**

```bash
# 方式 A：编辑 skill 根目录的 .env（推荐，详见 INSTALL.md）
# 方式 B：export 到当前 shell
export AI_API_BASE_URL="https://YOUR-API-HOST/v1"
export AI_API_KEY="YOUR_API_KEY"
export AI_MODEL="gpt-image-2"
```

`.env` 方式更便携，CI / 容器里依然能用 `export` 覆盖。

---

## 快速开始

### 1. 文生图

```bash
# 调用
python3 lib/client.py generate \
    --prompt "A modern minimalist PPT cover, blue gradient, abstract geometry, no text" \
    --size 16:9 \
    --format png \
    --out workspace/ppt_cover.png
```

输出：本地图片路径 + 远程 URL + 用量统计（tokens）。

### 2. 以图生图

```bash
python3 lib/client.py edit \
    --image workspace/ppt_cover.png \
    --prompt "Same layout but warm sunset color palette" \
    --size 16:9 \
    --out workspace/ppt_cover_v2.png
```

### 3. 蒙版编辑

蒙版要求：PNG，**白色 = 编辑区，黑色 = 保留区**，与原图同尺寸。

```bash
python3 lib/client.py edit \
    --image workspace/photo.png \
    --mask workspace/photo_mask.png \
    --prompt "Replace the masked sky with aurora borealis" \
    --out workspace/photo_aurora.png
```

### 4. 迭代工作流

skill 把每次生成都记录到 `workspace/history.jsonl`，可以：

```bash
# 列出历史
python3 lib/client.py history

# 复用某张图继续编辑
python3 lib/client.py edit \
    --image workspace/20260614_120000_abc.png \
    --prompt "..." \
    --strength 0.6
```

---

## 办公场景预设

直接用预设名，省去手算尺寸的麻烦。完整列表见 `presets/presets.json`，常用：

| 预设名 | 比例 | 像素 | 典型场景 |
|--------|------|------|----------|
| `ppt_cover_169` | 16:9 | 1536×896 | PPT 封面、Keynote 标题页 |
| `ppt_slide_169` | 16:9 | 1024×576 | PPT 内页插图 |
| `wechat_header` | 2.35:1 | 900×383 | 公众号文章头图 |
| `wechat_square` | 1:1 | 1080×1080 | 朋友圈方图 |
| `poster_a3` | √2:1 | 1240×1754 | A3 海报竖版 |
| `poster_a4` | √2:1 | 1240×1754 | A4 通知/传单 |
| `avatar_1k` | 1:1 | 1024×1024 | 微信/钉钉头像 |
| `avatar_2k` | 1:1 | 2048×2048 | 高清头像 |
| `banner_wide` | 4:1 | 1536×384 | 横幅广告 |
| `mobile_916` | 9:16 | 1024×1820 | 抖音/小红书竖屏 |
| `mobile_34` | 3:4 | 1024×1365 | 小红书图文 |
| `ecommerce_main` | 1:1 | 1024×1024 | 电商主图白底 |
| `logo_square` | 1:1 | 1024×1024 | Logo 底图（透明背景） |
| `redpacket_cover` | 9:16 | 1024×1820 | 微信红包封面 |
| `sticker_circle` | 1:1 | 1024×1024 | 表情包/贴纸 |
| `doc_inline` | 3:2 | 1536×1024 | 文档插图 |

调用：

```bash
python3 lib/client.py generate \
    --prompt "..." \
    --preset ppt_cover_169 \
    --format png \
    --out workspace/foo.png
```

`--preset` 和 `--size` 二选一，`--preset` 优先。

---

## 参数速查

### generate

| 参数 | 说明 | 默认 |
|------|------|------|
| `--prompt` | 必填，描述 | — |
| `--size` | `WxH` / `1:1` / `16:9` / `auto` | `1:1` |
| `--preset` | 预设名（覆盖 --size） | — |
| `--n` | 生成张数 | 1 |
| `--quality` | `standard` / `hd` | `standard` |
| `--format` | `png` / `jpg` / `webp` | `png` |
| `--background` | `transparent`（需 png/webp） | — |
| `--out` | 输出路径 | `workspace/<ts>.png` |

### edit

| 参数 | 说明 | 默认 |
|------|------|------|
| `--image` | 必填，输入图片路径（可重复多次） | — |
| `--mask` | 蒙版 PNG（可省略） | — |
| `--prompt` | 必填 | — |
| `--size` | 输出尺寸 | 跟输入图 |
| `--quality` | `standard` / `hd` | `standard` |
| `--format` | `png` / `jpg` / `webp` | 跟输入图 |
| `--n` | 生成张数 | 1 |
| `--out` | 输出路径 | `workspace/<ts>.png` |

---

## 工作流建议

**迭代改稿** 是日常最常用的模式：

1. 用 `generate` 出一张草图
2. 找到不顺眼的地方：让用户口头描述（"把天空换成极光""左边那个人戴红帽子"）
3. 走 `edit` + mask 局部改，或直接以图生图整体换风格
4. 记录所有版本到 `workspace/history.jsonl`，方便回滚
5. 最终选定版本导出为最终格式（jpg 压缩、webp 省体积）

**多版本提案**：用 `--n 4` 一次性出 4 张，挑喜欢的继续编辑。

**保留原图**：每次 `--out` 都给新文件名，skill 自动写历史，不要覆盖。

---

## 文件组织

```
apa/
├── SKILL.md           # 本文件
├── lib/
│   ├── client.py      # CLI 入口（generate / edit / history）
│   ├── api.py         # 纯函数 API 调用
│   ├── presets.py     # 预设加载
│   └── storage.py     # 历史记录 & workspace 管理
├── presets/
│   └── presets.json   # 办公场景预设表
├── bin/
│   └── gpt-image      # 全局调用软链（可选）
├── examples/          # 各类场景的 prompt 模板
├── samples/           # 10 张精选样图 + samples/README.md 索引
└── workspace/         # 所有生成图片 + history.jsonl
```

---

## 常见问题

**Q: 生图失败 / 返回错误？**
A: 检查 `AI_API_KEY` 是否过期；看 stderr 中的 HTTP 状态码和 API 错误体。

**Q: 生成的图带文字乱码？**
A: gpt-image-2 对文字渲染不稳定，prompt 末尾加 "no text, no letters, no characters"。

**Q: 想要高清图？**
A: 加 `--quality hd`，注意 token 消耗翻倍。

**Q: 透明背景？**
A: 加 `--background transparent`，必须配合 `--format png` 或 `webp`。

**Q: 以图生图效果不明显？**
A: 这是 gpt-image-2 的特点：参考图主要控制"主体和构图"，新 prompt 控制"风格和细节"。两者都写清楚才能稳定。
