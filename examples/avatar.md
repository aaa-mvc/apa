# 头像 / Sticker Prompt 模板

> **场景定位**：微信/钉钉/LinkedIn/邮件签名档
> **关键决策点**：① 真人 vs 卡通 ② 背景透明（PNG）vs 场景虚化 ③ 用途（严肃商务/轻松/品牌 IP）
> **常见坑**：写 `portrait of a man` 太模糊，模型给的样貌可能完全不像目标受众；务必写清年龄段 + 风格 + 镜头参数

头像 prompt 的核心：**主体清晰、表情自然、背景简洁、脸占画面 50% 以上**。

---

## 1. 商务男性头像

```bash
gpt-image generate \
  --prompt "Editorial fashion illustration portrait of a confident 38-year-old East Asian man, drawn in bold confident ink line art with soft watercolor washes, charcoal grey and muted teal palette with a single coral accent, sharp gaze toward camera, magazine cover composition, visible paper texture and slight ink bleed on edges giving an authentic hand-made feel, hand-painted background wash in dusty teal, 8K, no text, no letters" \
  --preset avatar_2k \
  --quality hd
```

**变体**：换年龄段 → 改 `35-year-old`；换风格 → 改 `navy blazer` 为 `turtleneck sweater` / `smart casual jacket`；换肤色 → 改 `East Asian` 为 `South Asian` / `Black` / `Latino`。

---

## 2. 商务女性头像

```bash
gpt-image generate \
  --prompt "Professional headshot of a friendly 32-year-old East Asian woman with shoulder-length hair, wearing a soft beige knit top, soft studio lighting with subtle rim light, blurred modern office background, gentle confident expression, sharp focus on face, no text, no letters" \
  --preset avatar_2k \
  --quality hd
```

---

## 3. 创意职业（设计师 / 摄影师 / 自由职业）

```bash
gpt-image generate \
  --prompt "Casual creative professional headshot, a 28-year-old man with curly hair and round glasses, wearing a sage green linen shirt, natural daylight, soft bokeh background of plants and warm wood, candid natural smile, shot on 50mm lens, no text, no letters" \
  --preset avatar_2k \
  --quality hd
```

---

## 4. Q 版 / Chibi 卡通

```bash
gpt-image generate \
  --prompt "Adorable chibi-style avatar of a young female software developer with short purple hair, large expressive eyes, wearing an oversized hoodie, soft pastel pink background, kawaii illustration style, clean vector look, no text, no letters" \
  --preset avatar_1k \
  --background transparent \
  --format png
```

> **透明背景** + `png` 才能当表情用。

---

## 5. 专业人士（医生 / 律师 / 学者）

```bash
gpt-image generate \
  --prompt "Professional headshot of a 45-year-old male doctor in a white coat with stethoscope, kind and trustworthy expression, soft clinical lighting, blurred hospital corridor background, sharp focus on face, no text, no letters" \
  --preset avatar_2k \
  --quality hd
```

---

## 6. 节日头像（春节）

```bash
gpt-image generate \
  --prompt "Festive Chinese New Year avatar, cute cartoon character wearing a red tangzhuang with gold embroidery, holding a small red envelope, warm red and gold background with subtle plum blossom pattern, joyful expression, illustration style, no text, no letters, no characters" \
  --preset avatar_1k \
  --background transparent \
  --format png
```

---

## 7. 家庭 / 亲子

```bash
gpt-image generate \
  --prompt "Warm family photo style, a parent and a young child in matching soft beige sweaters laughing together, soft natural light from window, blurred cozy living room background, shot on 35mm lens, candid joyful moment, no text, no letters" \
  --preset avatar_2k \
  --quality hd
```

---

## 迭代改稿的标准动作

```bash
# 卡通 → 真人
gpt-image edit --image workspace/<avatar>.png \
  --prompt "Convert this cartoon character to a realistic photographic portrait, same composition and pose, natural skin texture, soft studio lighting, no text" \
  --preset avatar_2k \
  --quality hd

# 换季节
gpt-image edit --image workspace/<avatar>.png \
  --prompt "Keep the same person and composition. Change the wardrobe to autumn: warm camel coat and burgundy scarf, autumn foliage bokeh in the background, no text" \
  --preset avatar_2k

# 换职业风格
gpt-image edit --image workspace/<avatar>.png \
  --prompt "Keep the same face and pose. Change to a tech startup founder aesthetic: black t-shirt, modern co-working space background with neon accent lighting, no text" \
  --preset avatar_2k
```
