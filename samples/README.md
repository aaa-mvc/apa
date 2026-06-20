# Samples · 10 张精选样图

> **所有 10 张都按 "抗 AI 痕迹 / 手作感" 思路出图** —— 用 watercolor / paper craft / marker line art / Memphis 配色把"塑料感"压下去。
> 每一张都对应 `examples/` 里的一个 prompt 模板，可以直接 copy-paste 修改。

## 抗 AI 关键词工具箱

| 关键词族 | 用法 | 适用场景 |
|----------|------|----------|
| `hand-painted texture` / `visible brush strokes` / `ink bleeds` | 写进 prompt 主段 | 插画、封面、贴纸、海报 |
| `Memphis design color palette` | 写进 prompt 配色段 | 商务类、活泼类、年轻向 |
| `slight paper grain throughout` / `cold-press paper` / `rice paper` | 写进 prompt 质感段 | 几乎所有需要"印刷感"的图 |
| `paper craft` / `hand-cut paper` / `hand-torn paper edges` | 写进 prompt 工艺段 | logo、icon、3D 主体 |
| `colored pencil shading` / `marker line art` / `wobbly outlines` | 写进 prompt 线条段 | 头像、贴纸、Q 版 |
| `deckled paper edges` / `analog film grain` | 写进 prompt 边角段 | 海报、复古向 |
| `visible brush strokes and color bleeds` | 写进 prompt 主段 | 美食、产品特写 |
| `no vector art` / `no clean digital look` / `no smooth gradients` | 写进负面提示 | 贴纸、IP 角色 |

> 提示：每个 prompt 加 2-3 个关键词就够，不要堆太多。

## 01 · skill 宣传海报（机器人 mascot）

```bash
gpt-image generate \
  --prompt "Isometric 3D illustration of a friendly retro robot mascot with a single cyclops eye and rounded body, wearing a beret and a striped scarf, sitting cross-legged on a stack of giant colored pencils, painting a vibrant landscape on a floating canvas screen with a paintbrush, small polaroid-style cards with tiny generated landscape thumbnails floating around, Memphis design color palette of teal, coral, mustard yellow and cream, hand-painted texture with visible brush strokes, slight paper grain throughout, 8K, illustration, no text, no letters, no characters, no words" \
  --preset ppt_cover_169 --quality hd --format png
```

**抗 AI 关键词实战**：`hand-painted texture with visible brush strokes` / `slight paper grain throughout` / `Memphis design color palette` / `isometric 3D illustration` —— 把"塑料感"压下去。

## 图例

| #  | 文件 | 场景 | 预设 | 质量 | 关联模板 |
|----|------|------|------|------|----------|
| 01 | `01-skill-intro-poster.png` | **skill 宣传海报**（机器人 mascot + 孟菲斯色） | `ppt_cover_169` | hd | — |
| 02 | `02-ppt-cover-neural-network.png` | PPT 封面 · 手绘神经网络（ink line + Memphis 配色） | `ppt_cover_169` | hd | [`examples/ppt_cover.md` §2](../examples/ppt_cover.md) |
| 03 | `03-ppt-cover-paper-craft.png` | PPT 封面 · 纸艺折纸球（hand-cut paper craft） | `ppt_cover_169` | hd | [`examples/ppt_cover.md` §7](../examples/ppt_cover.md) |
| 04 | `04-ppt-slide-watercolor-divider.png` | PPT 章节分隔 · 单笔水墨（cold-press 水彩纸） | `ppt_slide_169` | standard | [`examples/ppt_slide.md` §1](../examples/ppt_slide.md) |
| 05 | `05-avatar-editorial-illustration.png` | 商务男性头像 · 编辑插画风（ink + watercolor wash） | `avatar_2k` | hd | [`examples/avatar.md` §1](../examples/avatar.md) |
| 06 | `06-poster-environmental-watercolor.png` | 公益环保海报 · 复古插画（deckle edges + 水彩） | `poster_a3` | hd | [`examples/poster.md` §7](../examples/poster.md) |
| 07 | `07-social-douyin-cover.jpg` | 抖音竖屏封面 · 手绘赛博朋克（ink + flat color + ink bleeds） | `mobile_916` | standard | [`examples/social.md` §5](../examples/social.md) |
| 08 | `08-ecommerce-chocolate-truffle.png` | 食品特写 · 手绘纸面背景（visible brush strokes + film grain） | `mobile_34` | hd | [`examples/ecommerce.md` §3](../examples/ecommerce.md) |
| 09 | `09-logo-tech-paper-craft.png` | 科技初创 logo · 剪纸工艺（torn paper edges + fiber texture） | `logo_square` | standard | [`examples/logo.md` §2](../examples/logo.md) |
| 10 | `10-sticker-kawaii-shiba.png` | 萌系柴犬贴纸 · 手绘马克笔（marker line + watercolor + colored pencil） | `sticker_circle` | standard | [`examples/sticker.md` §1](../examples/sticker.md) |

> **怎么生成的**：用 `./bin/gpt-image --workspace samples generate --prompt ... --preset ...` 一条命令一张图。
> **token 消耗**：standard 平均 ~4,300 tokens/张，hd 翻倍到 ~6,300。
> **历史记录**：本目录不存 history.jsonl，运行时会在 `workspace/` 下自动生成。

## 怎么用这些样图

**1. 直接看效果**
打开 `02-ppt-cover-neural-network.png` 这类文件，对比 prompt 文字和实际出图，理解"抗 AI 关键词"组合能产生什么效果。

**2. 复制 prompt 微调**
打开 `examples/ppt_cover.md`，找到对应章节的代码块，把 `futuristic neural network` 替换成你的描述，主体词改一下就行。
记得**保留所有手作感关键词**（hand-painted / paper grain / ink bleeds），那是抗 AI 的核心。

**3. 用作"风格锚点"**
把样图作为参考图用 edit 派生新版本：

```bash
./bin/gpt-image --workspace samples edit \
  --image samples/02-ppt-cover-neural-network.png \
  --prompt "Same hand-drawn ink line art on cream paper with Memphis geometric accents. Change the subject to a glowing data dashboard instead of neural network" \
  --preset ppt_cover_169 \
  --quality hd
```

## 风格覆盖

| 维度 | 覆盖 |
|------|------|
| 色彩 | 孟菲斯 / 深蓝 / 青绿 / 暖金 / 冷暖对比 / 透明 |
| 主体 | 几何抽象 / 纸艺 / 人物 / 自然 / 食物 / logo / 表情 |
| 质感 | watercolor wash / ink line / paper craft / marker / colored pencil / film grain |
| 工艺 | hand-painted / hand-cut / hand-torn / hand-glued / hand-drawn |
| 纸张 | cold-press / rice paper / construction paper / deckled edges / 透明 PNG |
| 场景 | 商务 / 公益 / 社交 / 电商 / 品牌 / 贴纸 / 头像 |

你的需求如果在这 10 张范围内，可以直接复用 prompt；新场景按 `examples/` 里的五要素结构自己写一条，**记得加 2-3 个抗 AI 关键词**。
