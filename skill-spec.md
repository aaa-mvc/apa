# 生图 Skill 交付说明（gpt-image-2）

> 封装时间：2026-06-14
> API：`<YOUR-API-HOST>/v1` · `gpt-image-2`（OpenAI 兼容协议）
> 位置：`apa/`（推荐 clone 后改名）

---

## 一、能力概览

| 能力 | 接口 | 典型用途 |
|------|------|----------|
| 文生图 | `POST /v1/images/generations` | 从描述生成新图 |
| 以图生图 | `POST /v1/images/edits` | 基于参考图改风格/换主体/换场景 |
| 蒙版编辑 | `POST /v1/images/edits`（带 mask） | 局部重绘、抹掉水印、换背景 |
| 迭代修改 | 复用上一张图作为新输入 | "再画一版""换个颜色""改成夜晚" |

办公场景预设 **17 个**，覆盖 PPT 封面/内页、公众号头图/方图、A3/A4 海报、头像 1K/2K、4:1 Banner、9:16/3:4 移动端、电商主图、Logo、红包封面、表情包、文档插图。

支持多比例（1:1 / 3:2 / 2:3 / 16:9 / 9:16 / auto，非 1024 档自动就近归一）与多格式（PNG / JPG / WebP），覆盖办公所有常见场景。

---

## 二、环境配置

```bash
# 详见 INSTALL.md：推荐用 .env 配置
export AI_API_BASE_URL="https://YOUR-API-HOST/v1"
export AI_API_KEY="YOUR_API_KEY"
export AI_MODEL="gpt-image-2"
```

建议写入 `~/.zshrc` 持久化。

---

## 三、文件结构

```
apa/
├── SKILL.md              # 完整使用文档（参数速查、FAQ）
├── README.md             # 快速上手
├── bin/
│   └── gpt-image         # bash 入口（chmod +x）
├── lib/
│   ├── __init__.py
│   ├── client.py         # CLI 入口（generate / edit / history / preset）
│   ├── api.py            # 纯函数 OpenAI 兼容协议客户端
│   ├── presets.py        # 预设加载
│   └── storage.py        # 历史记录 & workspace 管理
├── presets/
│   └── presets.json      # 17 个办公场景预设 + 比例别名
├── examples/             # PPT/头像/海报 prompt 模板
└── workspace/            # 生成图片 + history.jsonl
```

---

## 四、常用调用

```bash
# 文生图（用预设）
./bin/gpt-image generate \
    --prompt "极简商务 PPT 封面，深蓝渐变，抽象几何" \
    --preset ppt_cover_169 \
    --format png

# 文生图（直接传尺寸）
./bin/gpt-image generate \
    --prompt "A modern minimalist PPT cover" \
    --size 16:9 \
    --quality hd

# 以图生图（迭代改稿）
./bin/gpt-image edit \
    --image workspace/test_city.png \
    --prompt "Convert this night scene to daytime, same composition" \
    --preset ppt_cover_169

# 蒙版编辑（局部重绘）
./bin/gpt-image edit \
    --image workspace/photo.png \
    --mask workspace/photo_mask.png \
    --prompt "Replace the masked sky with aurora borealis"

# 查历史 / 预设
./bin/gpt-image history --last 10 --verbose
./bin/gpt-image preset
./bin/gpt-image preset ppt_cover_169
```

---

## 五、参数速查

### generate

| 参数 | 说明 | 默认 |
|------|------|------|
| `--prompt` | 必填，描述 | — |
| `--size` | `WxH` / `1:1` / `16:9` / `auto` | `1024x1024` |
| `--preset` | 预设名（覆盖 `--size`） | — |
| `--n` | 生成张数 | 1 |
| `--quality` | `standard` / `hd` | `standard` |
| `--format` | `png` / `jpg` / `webp` | `png` |
| `--background` | `transparent`（需 png/webp） | — |
| `--out` | 输出路径 | `workspace/<ts>_gen.<ext>` |

### edit

| 参数 | 说明 | 默认 |
|------|------|------|
| `--image` | 必填，输入图路径（可重复多次） | — |
| `--mask` | 蒙版 PNG（白=编辑区，黑=保留） | — |
| `--prompt` | 必填 | — |
| `--size` | 输出尺寸 | 跟输入图 |
| `--quality` | `standard` / `hd` | `standard` |
| `--format` | `png` / `jpg` / `webp` | 跟输入图 |
| `--n` | 生成张数 | 1 |
| `--out` | 输出路径 | `workspace/<ts>_edit.<ext>` |

### history

| 参数 | 说明 |
|------|------|
| `--last N` | 只看最后 N 条 |
| `--verbose` / `-v` | 显示 prompt / parent / mask / url / tokens |

### preset

| 用法 | 说明 |
|------|------|
| `preset` | 列出全部预设 |
| `preset <name>` | 查看单个预设详情 |

---

## 六、办公场景预设表

| 预设名 | 尺寸 | 比例 | 格式 | 场景 |
|--------|------|------|------|------|
| `ppt_cover_169` | 1536×1024 | 16:9 | png | PPT 封面、Keynote 标题页 |
| `ppt_slide_169` | 1024×576 | 16:9 | png | PPT 内页插图 |
| `ppt_chart` | 1536×1024 | 3:2 | png | PPT 配图 |
| `wechat_header` | 1536×640 | 2.4:1 | jpg | 公众号文章头图 |
| `wechat_square` | 1024×1024 | 1:1 | jpg | 朋友圈方图 |
| `poster_a3` | 1024×1450 | A3 竖 | png | A3 海报 |
| `poster_a4` | 1024×1450 | A4 竖 | png | A4 通知/传单 |
| `avatar_1k` | 1024×1024 | 1:1 | png | 微信/钉钉头像 |
| `avatar_2k` | 1024×1024 | 1:1 | png | 高清头像 |
| `banner_wide` | 1536×384 | 4:1 | png | 横幅广告 |
| `mobile_916` | 1024×1820 | 9:16 | png | 抖音/小红书竖屏 |
| `mobile_34` | 1024×1365 | 3:4 | png | 小红书图文 |
| `ecommerce_main` | 1024×1024 | 1:1 | png（透明） | 电商主图白底 |
| `logo_square` | 1024×1024 | 1:1 | png（透明） | Logo 底图 |
| `redpacket_cover` | 1024×1820 | 9:16 | png | 微信红包封面 |
| `sticker_circle` | 1024×1024 | 1:1 | png（透明） | 表情包/贴纸 |
| `doc_inline` | 1536×1024 | 3:2 | png | 文档插图 |

**比例别名**（可直接用 `--size`）：`1:1 / square`、`3:2 / landscape`、`2:3 / portrait`、`16:9 / wide`、`9:16`、`auto`。

---

## 七、迭代工作流（推荐）

```
1. 选预设        ppt_cover_169 / wechat_header / avatar_1k ...
2. 写 prompt     主体 + 风格 + 构图 + 留白（末尾加 "no text"）
3. 第一次生成    --n 4 一次看多张，挑喜欢的
4. 迭代改稿      edit + 文字描述  OR  edit + mask 局部重绘
```

每次结果都存到 `workspace/` 并写入 `workspace/history.jsonl`，记录 prompt / parent / mask / url / tokens / elapsed_sec，可回看、复用、对比。

**示例：客户反复改稿**

```bash
# 草图
./bin/gpt-image generate --prompt "商务封面" --preset ppt_cover_169

# 客户嫌太冷，改暖
./bin/gpt-image edit --image workspace/<file>.png \
    --prompt "Same layout, change to warm sunset orange palette" \
    --preset ppt_cover_169

# 客户嫌 logo 区太大 → mask 局部重绘
./bin/gpt-image edit --image workspace/<file>.png \
    --mask workspace/logo_mask.png \
    --prompt "Replace masked area with abstract mountain silhouette"
```

---

## 八、端到端测试结果

| # | 场景 | 耗时 | tokens | 结果 |
|---|------|------|--------|------|
| 1 | generate + preset + transparent bg（电商苹果） | 29.5s | 4193 | 1254×1254 PNG，红苹果干净 |
| 2 | edit（苹果 → 梵高星空风格） | 77.6s | 4966 | 主体保持 + 笔触背景，效果惊艳 |
| 3 | edit + mask（苹果加绿叶） | 43.5s | 4952 | 绿叶无缝嵌入 |
| 4 | generate + HD quality（赛博朋克夜景） | 48.7s | 6267 | 1536×1024 HD |
| 5 | edit（夜景 → 白天） | 48.3s | 7376 | 构图完全一致 |
| 6 | history --verbose | < 0.1s | — | 正确记录 parent/usage/url |

---

## 九、常见问题（FAQ）

**Q: 生图失败 / 返回错误？**
A: 检查 `AI_API_KEY` 是否过期；看 stderr 中的 HTTP 状态码和 API 错误体。

**Q: 生成的图带文字乱码？**
A: gpt-image-2 对文字渲染不稳定，prompt 末尾加 "no text, no letters, no characters"。

**Q: 想要高清图？**
A: 加 `--quality hd`，注意 token 消耗翻倍。

**Q: 想要透明背景？**
A: 加 `--background transparent`，必须配合 `--format png` 或 `webp`。

**Q: 以图生图效果不明显？**
A: 这是 gpt-image-2 的特点：参考图主要控制"主体和构图"，新 prompt 控制"风格和细节"。两者都写清楚才能稳定。

**Q: 想要 1024 之外的精确尺寸？**
A: gpt-image-2 实际只支持 `1024x1024 / 1024x1536 / 1536x1024 / auto`。`--size 900x600` 会被自动就近归一，并在 stderr 中提示。

**Q: 怎么把当前图继续改？**
A: 复制它的绝对路径传给 `--image`，或查 `history --verbose` 找 `parent` 字段。

---

## 十、Prompt 模板速查

**PPT 封面**

```bash
gpt-image generate --prompt "极简商务 PPT 封面，深蓝渐变，抽象几何线条，留白 70% 给标题，无文字" \
    --preset ppt_cover_169 --quality hd
```

**公众号头图**

```bash
gpt-image generate --prompt "城市夜景延时摄影，暖黄与冷蓝对比，横向延展构图，右下 20% 留白，无文字" \
    --preset wechat_header --format jpg
```

**头像**

```bash
gpt-image generate --prompt "Professional headshot of a friendly 30-year-old Asian businesswoman, soft studio lighting" \
    --preset avatar_1k --quality hd
```

**表情包**

```bash
gpt-image generate --prompt "Funny cartoon panda face with shocked expression, white outline, transparent background" \
    --preset sticker_circle --background transparent
```

**短视频封面**

```bash
gpt-image generate --prompt "竖屏短视频封面，惊讶的年轻女性特写，背景虚化为暖色霓虹街景，电影色调" \
    --preset mobile_916
```

更多模板见 `examples/` 目录：`ppt_cover.md` / `avatar.md` / `poster.md`。
