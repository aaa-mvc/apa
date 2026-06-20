# 社交媒体配图 Prompt 模板

> **场景定位**：公众号头图、朋友圈、小红书、抖音/B站封面
> **关键决策点**：① 平台尺寸（公众号 2.4:1、抖音 9:16、小红书 3:4）② 视觉风格（生活感 / 高级感 / UGC）③ 留白位置
> **常见坑**：横版图把主体放中间 → 标题压在脸上；生活感过头变成"游客照"

社交媒体配图的关键：**有"人味儿"或"场景感"，不要过度设计**。

---

## 1. 公众号头图（城市夜景）

```bash
gpt-image generate \
  --prompt "Wide editorial-style cityscape at night, illuminated skyline reflected on calm river, warm sodium streetlights contrasting with cool blue sky, long-exposure motion blur on passing boats, horizontal composition with main subject in left two-thirds and ample clean sky in the right third for a headline, cinematic color grading, no text, no letters, no characters" \
  --preset wechat_header \
  --format jpg
```

**变体**：季节切换 → 末尾加 `light snow falling` / `autumn foliage in foreground` / `cherry blossoms at the riverbank`；时段切换 → `golden hour` / `blue hour` / `overcast morning`。

---

## 2. 公众号头图（自然 / 生活方式）

```bash
gpt-image generate \
  --prompt "Soft lifestyle photography, a sunlit wooden cabin in a misty mountain valley at dawn, gentle warm light filtering through pine trees, slightly desaturated earthy color palette, generous blurred foreground of wildflowers, horizontal composition, no text, no letters" \
  --preset wechat_header \
  --quality hd
```

---

## 3. 朋友圈九宫格

```bash
# 单张：方图生活记录
gpt-image generate \
  --prompt "Square lifestyle photo, an overhead flat-lay of a weekend brunch on a linen tablecloth: croissant, pour-over coffee, fresh berries, an open book, natural morning window light, soft shadows, slightly warm color temperature, no text, no letters" \
  --preset wechat_square \
  --format jpg
```

> 朋友圈九宫格技巧：先生成 9 张不同主体（咖啡、书、植物、城市一隅……），裁成相同尺寸，拼成 3×3。

---

## 4. 小红书图文（治愈 / 生活方式）

```bash
gpt-image generate \
  --prompt "Vertical lifestyle photo, a pair of hands holding a steaming matcha latte in a ceramic cup, sitting on a sunlit windowsill with a small succulent, soft natural light from the left, shallow depth of field, warm cream and sage green color palette, vertical 3:4 composition with negative space at top for headline, no text, no letters" \
  --preset mobile_34 \
  --quality hd
```

**变体**：换主语 → `holding a fresh croissant` / `holding a book with a bookmark` / `petting a sleeping cat`；换场景 → `on a wooden table in a cozy café` / `on a balcony overlooking a city`。

---

## 5. 抖音竖屏封面

```bash
gpt-image generate \
  --prompt "Vertical illustrated viral cover, hand-drawn portrait of a young woman with bold avant-garde makeup split between natural skin and neon cybernetic patterns, bold confident ink line art with flat color fills in cyan, coral, and mustard yellow, Tokyo street silhouettes in the background drawn in loose expressive strokes, hand-painted gradient sky in dusty rose and electric blue, slight paper texture and ink bleeds giving authentic craft feel, 8K, 9:16, no text, no letters" \
  --preset mobile_916 \
  --format jpg
```

> **爆款封面三要素**：人物大脸 + 强情绪 + 模糊背景，与上同。

**变体**：
- 美食：换成 `extreme close-up of noodles being lifted with chopsticks, steam rising`
- 旅行：换成 `wide vertical shot of a person standing at the edge of a turquoise lagoon, back to camera`
- 知识：换成 `close-up of hands writing in a notebook with coffee and books around`

---

## 6. B 站横屏封面

```bash
gpt-image generate \
  --prompt "Wide horizontal video thumbnail, a dramatic cinematic still of a person standing at the end of a long neon-lit cyberpunk alley, atmospheric fog, strong leading lines drawing the eye to the subject, moody teal and magenta color grading, horizontal 16:9 with the subject off-center to leave space for a title in the upper-left, no text, no letters" \
  --preset ppt_cover_169 \
  --quality hd
```

---

## 7. 节日祝福图

```bash
gpt-image generate \
  --prompt "Vertical Chinese New Year greeting card illustration, plum blossoms in full bloom with soft pink petals drifting in the wind, traditional ink-wash style, gold foil accents on branches, large empty central area for a blessing message, warm beige and crimson color palette, no text, no letters, no characters" \
  --preset mobile_916 \
  --format png
```

**变体**：中秋 → `full moon over a serene lake, soft mist, jade rabbit silhouette`；圣诞 → `cozy fireplace scene with warm bokeh lights, soft snow falling`；生日 → `pastel balloons and confetti explosion on a soft pink background`。

---

## 通用工作流

1. 先 `--n 4` 一次性出 4 张，挑构图
2. 用 `edit` 调色调（明确写 `same composition, change palette to...`）
3. 用 `edit` 调主体（明确写 `replace the main subject with...`）
4. 最终选定版本用 `--quality hd` 重出一次拿到高清
