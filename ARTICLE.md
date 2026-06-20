# AI 生图终极指南：用这 7 个要素，告别"一眼 AI"的塑料感

> 别再用"好看、高清、4K"写 prompt 了。这篇文章教你一套可复用的框架，让你的 AI 生图从"一看就是 AI 画的"变成"这是谁家设计师手绘的"。

---

## 为什么你生成的图一看就是 AI 画的？

AI 生图有个悖论：越让它"完美"，它越假。

你输入的 prompt 是 `beautiful landscape, high quality, 4K, realistic`——模型理解的"美"是光滑渐变、矢量级别的干净、3D 渲染般的精确。这些东西构成了我们常说的"塑料感"。

真正让人舒服的图像，恰恰相反：有纸张肌理、有笔触、有色彩的溢出、有线条的颤动。**设计感来自不完美。**

我用 75 次实战验证了一套框架，核心就两件事：

1. **一个七要素骨架**——每次写 prompt 按这个填
2. **一组"手作感"关键词**——把塑料感压下去

---

## 骨架：7 个要素，每次照填就行

```
[主体] + [风格] + [构图] + [光线] + [色彩] + [留白] + [负面提示]
```

不要偷懒写成 `a beautiful cat`。拆开：

| 要素 | 你填什么 | 例子 |
|------|---------|------|
| 主体 | 画什么 | `a tabby cat sleeping on a windowsill` |
| 风格 | 怎么画 | `hand-drawn ink sketch`（手绘）或 `editorial photography`（摄影） |
| 构图 | 东西放哪 | `cat on the left third, rest empty` |
| 光线 | 光源 | `soft morning light through sheer curtains` |
| 色彩 | 色板 | `cream, dusty rose, warm gray` |
| 留白 | 文字位置 | `top two-thirds empty for headline` |
| 负面提示 | 不要啥 | `no text, no smooth gradients, no 3D render look` |

**写完这七段，你的 prompt 已经从 10 分涨到了 70 分。**

---

## 杀手锏：手作感关键词工具箱

这是整篇文章最有价值的部分。以下关键词加到你的 prompt 里，AI 画出来的东西就不再"光滑得刺眼"：

### 质感（二选一）
```
hand-painted texture, visible brush strokes     ← 手绘感
film grain, analog photography                   ← 胶片感
```

### 纸张（必选一个）
```
cold-press watercolor paper   ← 水彩纸
rice paper texture            ← 宣纸
cream paper                   ← 奶油色纸
```

### 工艺
```
paper craft （纸艺）
hand-torn paper edges （手撕边缘）
bold ink line art （粗墨线）
```

### 配色（最百搭）
```
Memphis palette: teal, coral, mustard yellow, cream
```
孟菲斯配色天生有"设计师感"，不管画什么，加这个色板立刻提升质感。

### 反 AI 负面提示（每条必加）
```
no vector art, no clean digital look, no smooth gradients,
no 3D render, no airbrush smoothness, no text, no letters
```

**组合公式（直接抄）：**

| 场景 | 组合 |
|------|------|
| 海报/封面 | `hand-painted texture + paper grain + Memphis palette` |
| Logo/图标 | `paper craft + hand-torn edges + visible fibers` |
| 头像/贴纸 | `marker line art + watercolor fills + wobbly outlines` |
| 美食/产品 | `visible brush strokes + film grain + natural light` |

---

## 实战：从烂 prompt 到好 prompt

### Before（典型的烂 prompt）
```
a beautiful flower, high quality, 4K
```

### After（用框架重写）
```
A single dried rose on a sunlit windowsill. Hand-painted watercolor
style, visible brush strokes, cold-press paper texture. Soft morning
light from left. Memphis palette: dusty rose, sage green, warm cream.
Top half empty for headline. No text, no vector art, no 3D render.
```

**差别在哪？**第一个丢给 AI，你会得到一支光滑得像塑料的玫瑰。第二个，看起来像有人在纸上画了一幅水彩。

---

## 快速速查：9 个场景的起手式

| 场景 | 风格关键词 | 比例 | 留白 |
|------|-----------|------|------|
| PPT 封面 | `hand-drawn 2D flat, bold ink line art, Memphis accents` | 16:9 | 上 2/3 留白放标题 |
| 公众号头图 | `editorial photography, illuminated skyline, long exposure` | 2.4:1 | 右 1/3 留白 |
| 小红书封面 | `soft lifestyle, sunlit, desaturated earthy, shallow DOF` | 3:4 | 上下各留 15% |
| 抖音竖屏 | `neon cyberpunk, leading lines, cinematic color grading` | 9:16 | 下 1/3 留白 |
| 电商主图 | `premium product photo, pure white background, studio light` | 1:1 | 中央留白放 logo |
| 商务头像 | `editorial illustration, bold ink, watercolor washes` | 1:1 | 脸占 50% |
| 科技 Logo | `paper craft, layered geometry, hand-torn edges` | 1:1 | `no text, no letters` |
| 表情贴纸 | `kawaii, marker line art, watercolor fills, outline` | 1:1 | `no background` |
| 宽幅 Banner | `abstract 3D glass panels, gradient, left 2/3 empty` | 4:1 | 主体放右侧 |

---

## 迭代改稿的标准指令

改图比生成更常用。记住这几句标准模板：

```
换色："Keep exact composition. Change palette to [新配色]. No text."
换风格："Convert to [新风格]. Same layout, same color temperature."
换主体："Same style, same palette. Replace subject with [新主体]."
派生同系列："Same palette and style. Lower density, larger negative space."
```

---

## 最后

这篇文章的框架来自 75 条实战验证的 prompt。不是理论，是打出来的经验。

如果你用这套方法论，可以搭配 CLI 工具一键生成：**[github.com/aaa-mvc/apa](https://github.com/aaa-mvc/apa)**——内置 17 个办公预设和本文的全部模板。

记住一句话：**AI 生图不是让机器画得更完美，是让它画得更像人。**

---

*原文框架思路借鉴自 ABinya 的 picture-skill 项目 prompt 模板。本文所有文字、案例、表达均为原创。*
