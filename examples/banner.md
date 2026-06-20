# Banner / 长条广告 Prompt 模板

> **场景定位**：网页顶部、邮件头图、公众号关注引导、招聘 banner
> **关键决策点**：① 比例（4:1 / 16:9 / 16:5）② 视线引导（强 vs 弱）③ 主体位置
> **常见坑**：banner 太"满"反而没有焦点；颜色太杂在窄长条里显脏

Banner 的命脉：**强主体 + 留白 + 视觉引导线**。

---

## 1. Web 顶部 banner（产品官网）

```bash
gpt-image generate \
  --prompt "Modern SaaS product website hero banner, a stylized abstract 3D shape of layered translucent glass panels floating in the right third, soft gradient from white on the left to pale lavender on the right, generous empty left two-thirds for headline, clean minimal design, no text, no letters, no characters" \
  --preset banner_wide \
  --format png
```

**变体**：金融 → `dark navy with subtle gold accent lines and abstract chart pattern`；教育 → `soft cream with floating geometric shapes in coral and teal`；电商 → `vibrant pink-to-orange gradient with floating product silhouettes`。

---

## 2. App 启动屏 / 开屏

```bash
gpt-image generate \
  --prompt "Mobile app launch screen, a single elegant abstract gradient flowing from deep indigo to soft pink, with a large glowing orb in the center-right, ample negative space, vertical 9:16, premium and modern feel, no text, no logo, no letters" \
  --preset mobile_916 \
  --quality hd
```

---

## 3. 邮件头图

```bash
gpt-image generate \
  --prompt "Friendly email header image, an overhead shot of a wooden desk with a laptop, coffee mug, and a small plant, soft natural daylight, warm muted tones, horizontal 4:1 with the desk on the right and clean empty space on the left, no text, no letters, no screen content" \
  --preset banner_wide \
  --format jpg
```

---

## 4. 公众号关注引导

```bash
gpt-image generate \
  --prompt "WeChat follow-prompt banner, soft warm gradient from peach to cream, a stylized hand holding a smartphone in the lower-right corner with a glowing QR code area, abstract decorative dots and lines scattered subtly, no text, no letters, no QR code, no characters" \
  --preset banner_wide \
  --format png
```

> **不写 no QR code** → 模型可能直接画一个二维码占位，反而挡画面。

---

## 5. 招聘 banner

```bash
gpt-image generate \
  --prompt "Modern tech hiring banner, abstract gradient from deep purple to electric blue, a stylized silhouette of a team of three people collaborating in the right half, dynamic light streaks crossing horizontally, generous empty left half for the job title, no text, no logo, no letters, no characters" \
  --preset banner_wide \
  --format png
```

---

## 6. 展会 / 活动 banner

```bash
gpt-image generate \
  --prompt "Conference event banner, abstract diagonal composition with overlapping translucent geometric shapes in coral, teal, and gold, dark charcoal background, slight grain texture, dynamic and professional, wide 4:1 with main visual on the right, no text, no letters, no characters" \
  --preset banner_wide \
  --format png
```

---

## 7. 电商首页 banner

```bash
gpt-image generate \
  --prompt "E-commerce homepage banner, a vibrant gradient from hot pink to deep purple, abstract floating shopping-related icons (bag, tag, gift box) in low opacity scattered across the banner, central focal point with a glowing circular spotlight, wide 4:1, energetic and modern, no text, no letters, no numbers" \
  --preset banner_wide \
  --format png
```

---

## 8. 横幅广告 / 户外

```bash
gpt-image generate \
  --prompt "Outdoor advertising banner, a single bold product silhouette (a running shoe) dramatically lit from the side, dark gradient background, motion blur suggesting speed, vibrant accent color (electric orange), wide 4:1 with the shoe positioned right of center, no text, no logo, no letters, no brand marks" \
  --preset banner_wide \
  --quality hd
```

---

## Banner 的"留白原则"

横向 banner **永远把主体放在右 1/3 或左 1/3**，中间留白放标题。

```bash
# 左 1/3 主体
gpt-image generate \
  --prompt "...main subject in the left third, generous empty space in the right two-thirds..." \
  --preset banner_wide

# 右 1/3 主体
gpt-image generate \
  --prompt "...main subject in the right third, generous empty space in the left two-thirds..." \
  --preset banner_wide
```

如果你给的 prompt 主体在中间，文字就只能压在主体上，效果差。
