# PPT 内页 / 分隔页 Prompt 模板

> **场景定位**：章节分隔、数据背景、引言页、致谢页的内页视觉
> **关键决策点**：① 元素密度（内页必须 < 封面）② 主体在左/右/中（决定标题落点）③ 是否带人物/图标
> **常见坑**：元素太抢戏反而盖过文字；颜色和封面不一致导致整套 PPT 风格割裂

内页 prompt 关键：**低饱和 + 大留白 + 单一焦点**，让标题文字成为主角。

---

## 1. 章节分隔页（大数字 + 几何）

```bash
gpt-image generate \
  --prompt "Minimalist hand-painted watercolor section divider, a single thick brush stroke of slate blue bleeding vertically down on cold-press watercolor paper, soft natural pigment pooling at the bottom, visible paper fiber texture throughout, generous negative space on the left for a large title, 8K, no text, no letters, no numbers, no characters" \
  --preset ppt_slide_169 \
  --format png
```

---

## 2. 数据图表背景

```bash
gpt-image generate \
  --prompt "Abstract data visualization background, soft flowing wave lines in low-saturation teal and lavender, suggestion of a bar chart silhouette fading into the background, professional and subtle, gradient from white at top to very pale blue at bottom, no text, no labels, no axes, no numbers" \
  --preset ppt_slide_169
```

**变体**：要做"产品增长"叙事 → 把 `wave lines` 换成 `ascending curves`；要做"市场分析" → 换成 `concentric radar chart pattern`。

---

## 3. 引用页背景

```bash
gpt-image generate \
  --prompt "Elegant quote slide background, soft cream paper texture with subtle deckle edges, a single thin gold rule line in the upper third, ample negative space below for a long quote, classical and timeless feel, no text, no letters, no characters" \
  --preset ppt_slide_169
```

---

## 4. 时间线 / 路线图

```bash
gpt-image generate \
  --prompt "Subtle timeline background, a thin horizontal path crossing from left to right at one-third height, five small abstract milestone nodes evenly spaced along it, the path dissolves into soft particles at both ends, very pale gray on white, no text, no numbers, no labels" \
  --preset ppt_slide_169
```

---

## 5. 团队介绍页（人物剪影）

```bash
gpt-image generate \
  --prompt "Team introduction slide background, row of three abstract human silhouettes in low-opacity warm gray, soft gradient from cream to pale rose, modern and professional, large empty area on the right for bios, no text, no faces, no facial features, no characters" \
  --preset ppt_slide_169
```

> **注意**：写 `silhouettes` 比写 `people` 更稳，避免模型画具体人脸导致的版权/相似度问题。

---

## 6. 结尾致谢页

```bash
gpt-image generate \
  --prompt "Closing thank-you slide background, soft golden-hour landscape photo style with rolling hills and warm sunlight, very soft and out-of-focus, central composition, large negative space in the middle for a thank-you message, no text, no letters, no characters" \
  --preset ppt_slide_169 \
  --quality hd
```

---

## 7. Bullet 关键词背景

```bash
gpt-image generate \
  --prompt "Minimal keyword-list slide background, soft pastel coral color block filling the left third with subtle paper grain texture, remaining two-thirds pure white, large empty space for bullet points, modern Scandinavian design, no text, no letters, no numbers" \
  --preset ppt_slide_169
```

**变体**：换主色 → `sage green`、`dusty blue`、`warm beige`；换位置 → 把 `left third` 换成 `top third` 或 `bottom right corner`。

---

## 工作流建议

封面 + 内页最好**用同一份 prompt seed 派生**：

1. 先生成满意的封面
2. 用封面作为参考图 + `edit` + prompt 改成"低密度版本"（明确写 `lower density, larger negative space, subtle elements only`）
3. 几页内页共享同一色彩基调，整套 PPT 风格统一
