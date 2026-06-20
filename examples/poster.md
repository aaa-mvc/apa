# 海报 Prompt 模板

> **场景定位**：线下活动、产品发布、招聘、节日的视觉主视觉
> **关键决策点**：① 主体占比 ② 留白位置（决定文字落点）③ 视觉冲击力（强对比 vs 高级感）
> **常见坑**：竖版海报把主体放中间导致文字无处放；人物海报不写明风格会"出戏"

海报 prompt 的核心：**主视觉 + 大量负空间 + 强情绪**。

---

## 1. 产品发布会

```bash
gpt-image generate \
  --prompt "Sleek product launch poster, vertical, a single glowing futuristic device floating in the center, deep space-black background with subtle blue light rays emanating outward, dramatic top-down spotlight, large negative space at top and bottom for headlines, ultra-premium feel, no text, no letters, no logo" \
  --preset poster_a3 \
  --format png \
  --quality hd
```

---

## 2. 节日促销

```bash
gpt-image generate \
  --prompt "Festive sale poster, vertical, abundant red and gold confetti exploding from the upper-right corner, a single elegant gift box wrapped in gold ribbon in the lower third, dynamic motion blur on the confetti, large empty top half for the headline, no text, no letters, no numbers" \
  --preset poster_a3 \
  --format png
```

---

## 3. 招聘海报

```bash
gpt-image generate \
  --prompt "Modern hiring poster, vertical, a stylized abstract city skyline in the lower half with warm gradient from coral to deep purple, large empty upper two-thirds for the job title, a subtle paper grain texture throughout, professional and inviting, no text, no letters, no logo" \
  --preset poster_a3
```

---

## 4. 讲座 / 沙龙

```bash
gpt-image generate \
  --prompt "Intellectual lecture poster, vertical, soft warm overhead spotlight illuminating a single open book on a dark wooden table, atmospheric haze in the background, bottom third in shadow reserved for event details, moody and contemplative, no text, no letters" \
  --preset poster_a3 \
  --format png \
  --quality hd
```

---

## 5. 音乐节

```bash
gpt-image generate \
  --prompt "Vibrant music festival poster, vertical, abstract layered wave forms in neon pink, electric blue, and acid green, dynamic diagonal composition, slight grain and chromatic aberration for retro feel, dark background, large negative space in upper-left for the lineup, no text, no letters, no band names" \
  --preset poster_a3
```

---

## 6. 体育 / 运动会

```bash
gpt-image generate \
  --prompt "Dynamic sports event poster, vertical, abstract motion trails of a sprinter captured mid-stride, energetic diagonal composition, bold color blocks of orange and electric blue, slight grunge texture, large negative space at top for the event name, no text, no letters, no numbers" \
  --preset poster_a3
```

---

## 7. 公益 / 环保

```bash
gpt-image generate \
  --prompt "Vertical illustrated environmental awareness poster, hand-drawn ink line art of a tiny gnarled tree on a windswept cliff, soft watercolor washes of dawn pink, gold, and storm grey in the sky, hand-painted clouds with visible brush strokes, a tiny silhouette of a person at the base of the tree for scale, deckled paper edges giving a vintage broadside poster feel, slight paper grain throughout, 8K, no text, no letters" \
  --preset poster_a3 \
  --format png \
  --quality hd
```

---

## 8. 餐饮新品

```bash
gpt-image generate \
  --prompt "Restaurant new dish poster, vertical, a single elegantly plated signature dish in the lower third on a dark slate plate, dramatic side lighting, steam rising through soft bokeh background, large negative space at top for the dish name, no text, no letters, no menu" \
  --preset poster_a3 \
  --quality hd
```

---

## 蒙版替换工作流（局部更换主体）

```bash
# 先生成底版
gpt-image generate --prompt "Festival poster with crowd silhouette" --preset poster_a3

# 用蒙版只换主体（人头）→ 真人主角
gpt-image edit \
  --image workspace/<poster>.png \
  --mask workspace/crowd_mask.png \
  --prompt "Replace the masked area with a single confident young performer on stage under a spotlight" \
  --preset poster_a3
```

> 蒙版 PNG：白色 = 编辑区，黑色 = 保留区，与原图同尺寸。
