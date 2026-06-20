# Logo 底图 / 品牌视觉 Prompt 模板

> **场景定位**：logo 设计的"底图/氛围图"，不是真正的 logo 生成（文字 logo 还是得在 Figma/Illustrator 里手画）
> **关键决策点**：① 行业调性（餐饮/科技/医疗/教育）② 配色（单色 vs 多色）③ 是否需要透明背景
> **常见坑**：写 "logo design" 模型会试图画字母组合 → 必须明确说 `no text, no letters, abstract emblem only`

Logo 底图 prompt 的核心：**抽象图形 + 强烈行业属性 + 透明背景 + 极简留白**。

---

## 1. 餐饮 logo

```bash
gpt-image generate \
  --prompt "Abstract emblem for a coffee shop brand, a stylized coffee bean morphing into a leaf, deep forest green and warm copper color palette, centered composition with abundant negative space, modern minimal style, no text, no letters, no words, no characters" \
  --preset logo_square \
  --background transparent \
  --format png
```

**变体**：中餐 → `chopsticks meeting a stylized Chinese knot, vermillion and gold`；甜品 → `a soft swirl of cream and a cherry, pastel pink and white`；茶饮 → `an abstract tea leaf and a single water droplet, jade green and warm gold`。

---

## 2. 科技初创

```bash
gpt-image generate \
  --prompt "Hand-cut paper craft logo mark for a tech startup, layered geometric shapes in deep midnight navy and electric cyan with visible hand-torn paper edges giving an organic craft feel, slight shadows between the paper layers showing depth, golden ratio proportions, perfectly centered on transparent background, 8K clean render with subtle paper fiber texture, no text, no letters, no characters" \
  --preset logo_square \
  --background transparent \
  --format png
```

**变体**：AI 公司 → `concentric neural network nodes forming a sphere, indigo and white`；SaaS → `three ascending bars inside a rounded square, blue gradient`；硬件 → `a stylized circuit path forming the silhouette of a chip, dark silver and cyan`。

---

## 3. 教育培训

```bash
gpt-image generate \
  --prompt "Abstract emblem for an education brand, a stylized open book with a glowing graduation cap floating above, warm yellow and navy blue palette, friendly yet professional, generous negative space, no text, no letters, no numbers, no characters" \
  --preset logo_square \
  --background transparent \
  --format png
```

---

## 4. 医疗健康

```bash
gpt-image generate \
  --prompt "Abstract emblem for a healthcare brand, a stylized heart shape intertwined with a leaf, soft mint green and warm coral, modern minimal style, centered, abundant negative space, no text, no cross, no medical symbols, no letters" \
  --preset logo_square \
  --background transparent \
  --format png
```

> 写 `no cross, no medical symbols` 避免模型画红十字/蛇杖等明显医疗标识。

---

## 5. 文创 / 手作品牌

```bash
gpt-image generate \
  --prompt "Abstract emblem for a cultural creative brand, a stylized hand-drawn bird in flight, ink-wash style with subtle gold foil accents, warm beige and crimson, organic and artistic, square 1:1 with the bird centered, no text, no letters, no characters" \
  --preset logo_square \
  --background transparent \
  --format png
```

---

## 6. 宠物店

```bash
gpt-image generate \
  --prompt "Abstract emblem for a pet store brand, a minimalist silhouette combining a dog and cat in negative space, warm caramel and sage green, friendly and approachable, no text, no letters, no words" \
  --preset logo_square \
  --background transparent \
  --format png
```

---

## 7. 运动 / 健身

```bash
gpt-image generate \
  --prompt "Abstract emblem for a fitness brand, a stylized dynamic arrow piercing through a circle, deep charcoal and electric orange, high-energy and bold, square 1:1, no text, no letters, no characters" \
  --preset logo_square \
  --background transparent \
  --format png
```

---

## 8. 美业 / 美容

```bash
gpt-image generate \
  --prompt "Abstract emblem for a beauty brand, an elegant abstract flower with three soft petals, rose gold and blush pink, feminine and luxurious, perfectly centered with abundant negative space, no text, no letters, no characters" \
  --preset logo_square \
  --background transparent \
  --format png
```

---

## 实际工作流（AI 底图 + 手画 logo 文字）

```bash
# 1. AI 出底图（图形 / 调性）
gpt-image generate --prompt "..." --preset logo_square --background transparent

# 2. 拿到设计师/Figma 里叠 logo 字体和组合
# 3. 也可以用蒙版局部迭代
gpt-image edit --image workspace/<logo_bg>.png \
  --mask workspace/<part_mask>.png \
  --prompt "Replace the masked element with a more dynamic flowing curve" \
  --preset logo_square \
  --background transparent
```
