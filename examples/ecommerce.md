# 电商主图 / 详情页 Prompt 模板

> **场景定位**：淘宝/京东/抖音小店/小红书电商的主图、白底图、详情页头图
> **关键决策点**：① 背景（白底 vs 场景）② 主体占比（主图 70%+）③ 调性（高端 / 性价比 / 节日促销）
> **常见坑**：主图主体太小被文字压死；白底图背景不纯（带阴影/纹理）影响上架审核

电商图的命脉：**主体清晰、色彩纯正、构图可加文字**。

---

## 1. 3C 数码主图

```bash
gpt-image generate \
  --prompt "Premium product photo of a sleek wireless earbud case in matte black, centered in frame, three-quarter view, completely pure white background, soft studio lighting with subtle reflection underneath, ultra sharp focus on the product, no text, no logo, no shadow box" \
  --preset ecommerce_main \
  --background transparent \
  --format png
```

**变体**：手机/平板 → `front three-quarter view, screen facing camera, dark mode screen`；笔记本电脑 → `laptop open at 110 degree angle, screen showing abstract gradient wallpaper`。

---

## 2. 服饰白底图

```bash
gpt-image generate \
  --prompt "E-commerce product photo of a folded cashmere sweater in soft camel color, neatly arranged in the center, pure white seamless background, soft overhead lighting with no harsh shadows, crisp focus, fashion catalogue style, no text, no tags, no hangers" \
  --preset ecommerce_main \
  --background transparent \
  --format png
```

---

## 3. 食品特写

```bash
gpt-image generate \
  --prompt "Playful luxury food photography, a single artisan chocolate truffle rolling on a hand-painted paper-textured surface, dusted with 24K gold flakes and a hint of rare saffron, dramatic warm side lighting revealing truffle micro-texture, dark moody background painted in loose visible brush strokes of indigo and burnt umber, slight analog film grain, hand-styled prop arrangement, 8K, vertical 3:4, no text, no plate" \
  --preset mobile_34 \
  --quality hd
```

**变体**：饮品 → `a glass of iced latte with condensation droplets, soft daylight`；烘焙 → `a freshly baked croissant with golden flaky layers, steam rising`。

---

## 4. 美妆 / 护肤品平铺

```bash
gpt-image generate \
  --prompt "Flat-lay product photography of a luxury skincare bottle and dropper on a marble surface, surrounded by delicate flower petals and water droplets, soft natural lighting from the left, muted earth tones, square 1:1 composition with the bottle as the focal point, no text, no labels, no logo" \
  --preset wechat_square \
  --quality hd
```

---

## 5. 家居场景

```bash
gpt-image generate \
  --prompt "Lifestyle product photo of a designer ceramic vase with dried pampas grass, placed on a wooden side table in a sunlit Scandinavian living room, warm natural light streaming through linen curtains, soft beige and cream palette, vertical 3:4 composition, no text, no logo" \
  --preset mobile_34 \
  --quality hd
```

---

## 6. 节日礼盒

```bash
gpt-image generate \
  --prompt "Festive gift box product photo, an elegant deep green gift box tied with a gold silk ribbon, sitting on a polished marble surface, soft bokeh of warm fairy lights in the background, vertical 3:4 composition, premium and celebratory mood, no text, no letters, no numbers" \
  --preset mobile_34 \
  --format png
```

---

## 7. 限时秒杀 Banner

```bash
gpt-image generate \
  --prompt "E-commerce flash sale banner, dynamic composition with abstract speed lines in red and gold rushing from right to left, a glowing shopping cart icon in the center, dark gradient background, high-energy and urgent feel, wide 4:1 with main subject slightly left of center, no text, no letters, no numbers" \
  --preset banner_wide \
  --format png
```

---

## 8. 详情页头图

```bash
gpt-image generate \
  --prompt "E-commerce product detail page hero image, a single product shot from an interesting low angle, dramatic lighting that emphasizes the product's premium material and craftsmanship, vertical 3:4 with the product filling two-thirds of the frame, dark gradient background, no text, no labels, no watermarks" \
  --preset mobile_34 \
  --quality hd
```

---

## 主图 vs 详情图的工作流

```bash
# 1. 干净白底主图（用于商品列表页/搜索结果）
gpt-image generate --prompt "..." --preset ecommerce_main --background transparent

# 2. 同款做场景图（用于详情页头图）
gpt-image edit --image workspace/<main>.png \
  --prompt "Keep the exact same product. Place it in a stylish minimalist lifestyle setting, on a wooden table with soft daylight, no text" \
  --preset mobile_34 \
  --quality hd
```

这样列表页和详情页视觉一致，但调性不同。
