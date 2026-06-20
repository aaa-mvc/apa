# 表情包 / 贴纸 Prompt 模板

> **场景定位**：聊天表情包、节日贴纸、公众号配图、社交媒体装饰
> **关键决策点**：① 风格（卡通 / 萌系 / 写实）② 透明背景（PNG）③ 留白裁切
> **常见坑**：模型把表情画在中间但占满全图 → 裁切后边距不够；写"白底"反而会带阴影

贴纸的命脉：**轮廓清晰 + 透明背景 + 单个主体 + 强情绪**。

---

## 1. 萌系表情（基础款）

```bash
gpt-image generate \
  --prompt "Hand-drawn kawaii sticker character, a baby Shiba Inu puppy with huge sparkling eyes and a tiny smile, drawn in bold confident marker line art with soft watercolor fills in cream, coral, and warm brown, visible brush strokes and slight color bleeds giving authentic hand-painted feel, isolated on pure transparent background, 8K, kawaii with handmade craft personality, no text, no letters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

**变体**：换动物 → `panda`, `shiba inu`, `corgi`, `hedgehog`, `red panda`；换情绪 → `sleeping`, `laughing`, `crying`, `angry`, `confused`, `winking`。

---

## 2. 节日贴纸（春节）

```bash
gpt-image generate \
  --prompt "Cute Chinese New Year sticker, a chubby cartoon tiger holding a red envelope, traditional tang suit, soft smile, surrounded by small gold ingots and plum blossoms, vibrant red and gold color palette, transparent background, illustration style, no text, no letters, no characters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

---

## 3. 萌宠表情

```bash
gpt-image generate \
  --prompt "Adorable Shiba Inu face sticker, head tilted to the side, tongue sticking out, big glossy eyes, soft cream background circular outline, photographic style with slight illustration overlay, transparent background, no text, no letters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

---

## 4. Emoji 风格（微信聊天用）

```bash
gpt-image generate \
  --prompt "Yellow emoji-style face sticker, exaggerated joyful crying expression, blue teardrop, hands on cheeks, classic flat emoji art style, transparent background, no text, no letters, no words" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

---

## 5. 文艺短句配图

```bash
gpt-image generate \
  --prompt "Minimalist decorative illustration, a single dried flower in a translucent glass vase, soft watercolor style, muted earth tone palette, vertical 9:16, transparent background, no text, no letters, no characters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

> 配文字的事交给剪映/Canva，AI 出配图就够。

---

## 6. 涂鸦风

```bash
gpt-image generate \
  --prompt "Hand-drawn doodle sticker set on transparent background, scattered cute little icons including a smiling sun, a sleeping moon, a tiny cactus, a coffee cup with steam, and a small lightning bolt, all in a consistent black ink line-art style with subtle color fills, no text, no letters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

> 想要单张就明确写 "single icon"；想要 set 就写 "set of multiple icons"。

---

## 7. 励志小语配图

```bash
gpt-image generate \
  --prompt "Flat illustration of a tiny hiker reaching the summit of a stylized triangular mountain at sunrise, soft orange and pink sky, gentle optimistic mood, square 1:1 with the figure positioned to leave space above, transparent background, no text, no letters, no characters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

---

## 8. IP 角色贴纸（品牌专用）

```bash
gpt-image generate \
  --prompt "Brand mascot character sticker, a cute cartoon avocado with arms and legs, big smile, wearing a tiny straw hat, standing pose, kawaii style with soft outlines, transparent background, no text, no logo, no letters" \
  --preset sticker_circle \
  --background transparent \
  --format png
```

**变体**：换主体 → `pear`, `mango`, `strawberry`, `bubble tea`；换动作 → `waving`, `giving thumbs up`, `dancing`, `sleeping`。

---

## 系列贴纸的"一致性"技巧

```bash
# 1. 先生成一张"标准款"，挑一个定下角色
gpt-image generate --prompt "..." --preset sticker_circle --background transparent

# 2. 用 edit 派生同款不同动作（明确写 keep the same character）
gpt-image edit --image workspace/<sticker>.png \
  --prompt "Same character, same style, same outline. Change the pose to waving both hands in the air, very excited, no text" \
  --preset sticker_circle \
  --background transparent
```

这样一套 6-8 张的角色贴纸，调性就是一致的。
