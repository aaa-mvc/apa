# PPT 封面 Prompt 模板

> **场景定位**：会议开场 / 路演开场 / 季度汇报的视觉门面
> **关键决策点**：风格（商务/科技/中式/扁平/3D）、色彩情绪（冷峻/温暖/中性的）、留白比例（60–80% 给标题）
> **常见坑**：① 风格元素堆太多反而乱 ② 配色和品牌冲突 ③ 主体居中导致标题没地方放

每个 prompt 都按 "主体 / 风格 / 构图 / 光线 / 色彩 / 留白 / 负面提示" 七要素写，可直接复制修改主体词。

---

## 1. 商务深蓝（最稳的默认）

```bash
gpt-image generate \
  --prompt "Epic cinematic corporate keynote cover, deep midnight blue to electric cobalt gradient sky, a single powerful beam of volumetric light slicing diagonally through atmospheric haze, distant geometric city silhouette dissolving into bokeh in the lower right, anamorphic lens flare with cyan and amber streaks, 8K hyper-detailed, shot on ARRI Alexa 65, cinematography inspired by Blade Runner 2049, generous negative space on the left two-thirds for title, no text, no letters, no characters, no logo" \
  --preset ppt_cover_169 \
  --format png \
  --quality hd
```

**变体**：要更"权威"，把 `diagonal light ray` 换成 `central radial glow`；要更"科技"，把 `bokeh` 换成 `circuit board texture in the corner`。

---

## 2. 科技蓝绿

```bash
gpt-image generate \
  --prompt "Hand-drawn 2D flat illustration of a futuristic neural network, bold ink line art on cream cold-press paper texture, Memphis-style geometric accents in teal, coral, and mustard yellow, slightly imperfect hand-drawn lines giving a craft-made feel, holographic nodes drawn as little glowing dots connected by hand-sketched pathways, abstract digital particles scattered like ink splatters, 8K, no text, no letters, no characters" \
  --preset ppt_cover_169 \
  --quality hd
```

**变体**：改成 AI/大模型主题 → 把 `circuit board` 换成 `neural network nodes`；改成新能源/电池 → 换成 `lithium crystal lattice`。

---

## 3. 新中式水墨

```bash
gpt-image generate \
  --prompt "New Chinese style presentation cover, distant ink-wash mountain landscape, rice paper texture with subtle warm beige tone, asymmetric composition with mountains in lower third, abundant negative space on top, soft natural lighting, no text, no letters, no characters, no seal" \
  --preset ppt_cover_169 \
  --format png
```

**变体**：想要更"古朴" → 末尾加 `with calligraphy brush stroke accents`；想要更"现代" → 把 `rice paper` 换成 `matte canvas`。

---

## 4. 极简白（互联网公司最爱）

```bash
gpt-image generate \
  --prompt "Ultra-minimalist presentation cover, pure off-white background, a single soft sage-green organic blob in the bottom-right quadrant, extremely subtle drop shadow, asymmetric composition, no text, no letters, no characters" \
  --preset ppt_cover_169
```

**变体**：换主色 → `soft terracotta`、`soft slate blue`、`soft butter yellow` 任选；想更有"动势" → 把 `blob` 换成 `flowing curve`。

---

## 5. 莫兰迪色块（适合女性向 / 美妆 / 教育）

```bash
gpt-image generate \
  --prompt "Modern presentation cover with overlapping Morandi color blocks (dusty pink, sage green, warm beige, soft terracotta), flat design, gentle grain texture, layered geometric composition filling right two-thirds, generous left negative space, no text, no letters, no characters" \
  --preset ppt_cover_169
```

---

## 6. 扁平插画商务

```bash
gpt-image generate \
  --prompt "Flat illustration presentation cover, abstract business scene with tiny figures in a stylized open-plan office, viewed from above at three-quarter angle, warm palette of coral, cream, and slate blue, isometric-style composition, no text, no letters, no characters" \
  --preset ppt_cover_169 \
  --format png
```

---

## 7. 3D 渲染光感（适合发布会/招商）

```bash
gpt-image generate \
  --prompt "Paper craft 3D scene of a single golden origami sphere floating in a deep teal paper-cut void, dramatic side lighting casting layered paper shadows on a hand-cut paper backdrop, visible torn paper edges and fibers on the sphere, hand-glued texture giving a real-world craft feel, Memphis-style geometric confetti scattered around, slight paper grain throughout, 8K, no text, no letters, no characters" \
  --preset ppt_cover_169 \
  --quality hd
```

**变体**：把 `sphere` 换成 `torus` / `crystal cluster` / `fluid droplet`，立刻换一个主题。

---

## 8. 暖色夕阳（季度总结 / 温情场景）

```bash
gpt-image generate \
  --prompt "Warm sunset presentation cover, soft golden-orange to dusty pink gradient sky, silhouetted city skyline in the lower third, lens flare from the setting sun, horizontal composition, cinematic color grading, no text, no letters, no characters" \
  --preset ppt_cover_169 \
  --format png
```

---

## 迭代改稿的标准动作

```bash
# 改主色调（冷 → 暖）
gpt-image edit --image workspace/<cover>.png \
  --prompt "Keep the exact same composition, layout, and elements. Change the entire color palette to warm sunset: deep orange, golden yellow, and dusty rose. No text." \
  --preset ppt_cover_169

# 改风格（写实 → 扁平）
gpt-image edit --image workspace/<cover>.png \
  --prompt "Convert this to flat vector illustration style. Keep the same layout and color temperature. No text." \
  --preset ppt_cover_169
```
