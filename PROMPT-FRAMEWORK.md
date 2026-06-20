# AI 生图 Prompt 框架 · 75 条模板提炼

> 适合投喂给 ChatGPT (DALL-E 3)、Gemini (Imagen) 或任何支持图像生成的 AI。
> 核心思路：**七要素骨架 + 场景关键词 + 抗 AI 手作感关键词**

---

## 一、统一骨架（每次写 prompt 按这 7 段填）

```
[主体] + [风格] + [构图/位置] + [光线] + [色彩] + [留白] + [负面提示]
```

| 段位 | 作用 | 示例 |
|------|------|------|
| 主体 | 画面里画什么 | `a futuristic neural network` / `a single artisan chocolate truffle` |
| 风格 | 怎么画 | `hand-drawn 2D flat illustration` / `editorial fashion illustration` |
| 构图 | 东西放哪 | `asymmetric composition` / `main subject in left third` |
| 光线 | 光源和氛围 | `dramatic side lighting` / `soft natural morning window light` |
| 色彩 | 色板和情绪 | `Memphis-style: teal, coral, mustard yellow` / `Morandi: dusty pink, sage green` |
| 留白 | 文字落点 | `generous negative space on top two-thirds for headline` |
| 负面提示 | 不要什么 | `no text, no letters, no characters, no logo` |

---

## 二、抗 AI 手作感关键词工具箱（每条 prompt 加 2-3 个）

### 质感类
```
hand-painted texture, visible brush strokes, ink bleeds, color bleeds,
slight paper grain throughout, analog film grain, subtle grain texture
```

### 工艺类
```
paper craft, hand-cut paper, hand-torn paper edges, hand-glued texture,
visible paper fibers, torn paper shadows
```

### 纸张类
```
cold-press watercolor paper, rice paper texture, deckled paper edges,
cream paper, construction paper, matte canvas
```

### 线条类
```
bold ink line art, marker line art, wobbly outlines, slightly imperfect hand-drawn lines,
colored pencil shading, loose expressive strokes
```

### 配色（孟菲斯风格——最百搭的抗 AI 配色）
```
Memphis design color palette: teal, coral, mustard yellow, cream
```

### 负面提示（赶走塑料感）
```
no vector art, no clean digital look, no smooth gradients,
no plastic texture, no 3D render look, no airbrush smoothness
```

### 组合公式
```
插画/封面/海报：hand-painted texture + paper grain + Memphis palette
logo/3D 主体：paper craft + hand-torn edges + fiber texture
头像/贴纸/Q 版：marker line art + watercolor fills + wobbly outlines
美食/产品特写：visible brush strokes + film grain + hand-painted background
```

---

## 三、9 大场景关键词速查表

### 1. PPT 封面（8 种风格）

| 风格 | 核心关键词 | 色彩 |
|------|-----------|------|
| 商务深蓝 | `cinematic corporate keynote, volumetric light, anamorphic lens flare, ARRI Alexa 65` | deep midnight blue → electric cobalt |
| 科技蓝绿（手绘）| `hand-drawn 2D flat illustration, bold ink line art, Memphis geometric accents, holographic nodes` | teal, coral, mustard yellow |
| 新中式水墨 | `ink-wash mountain landscape, rice paper texture, asymmetric composition` | warm beige, ink black |
| 极简白 | `ultra-minimalist, pure off-white, single soft organic blob, subtle drop shadow` | sage-green accent |
| 莫兰迪色块 | `overlapping Morandi color blocks, flat design, gentle grain, layered geometric` | dusty pink, sage green, warm beige |
| 扁平插画商务 | `flat illustration, abstract business scene, isometric-style, tiny figures` | coral, cream, slate blue |
| 纸艺 3D（折纸球）| `paper craft 3D, origami sphere, hand-cut paper, torn paper edges, Memphis confetti` | deep teal, gold |
| 暖色夕阳 | `golden-orange to dusty pink gradient, silhouetted city skyline, lens flare, cinematic color grading` | warm sunset |

**负面提示必加**：`no text, no letters, no characters, no logo`

---

### 2. PPT 内页（7 种模板）

| 模板 | 核心关键词 | 注意 |
|------|-----------|------|
| 章节分隔页 | `hand-painted watercolor, single thick brush stroke, cold-press paper, pigment pooling` | 元素密度 < 封面 |
| 数据图表背景 | `soft flowing wave lines, low-saturation, chart silhouette fading into background` | `no labels, no axes, no numbers` |
| 引用页背景 | `cream paper texture, deckle edges, single thin gold rule line, ample negative space` | 大量留白放文字 |
| 时间线/路线图 | `thin horizontal path, 5 milestone nodes, dissolves into soft particles at ends` | `no numbers, no labels` |
| 团队介绍页 | `row of 3 abstract silhouettes, low-opacity warm gray` | 用 `silhouettes` 不用 `people` |
| 结尾致谢页 | `soft golden-hour landscape, out-of-focus, rolling hills, warm sunlight` | 中央大量留白 |
| Bullet 关键词背景 | `pastel color block filling left third, paper grain, remaining two-thirds pure white` | 左侧色块可换色/换位置 |

**原则**：低饱和 + 大留白 + 单一焦点，让标题文字成为主角。

---

### 3. 海报（8 种场景）

| 场景 | 核心关键词 | 色彩/氛围 |
|------|-----------|----------|
| 产品发布会 | `glowing futuristic device floating, deep space-black, dramatic top-down spotlight` | 黑 + 蓝光束 |
| 节日促销 | `red and gold confetti exploding, elegant gift box, dynamic motion blur` | 红 + 金 |
| 招聘海报 | `stylized abstract city skyline, warm gradient, paper grain texture` | coral → deep purple |
| 讲座/沙龙 | `soft overhead spotlight, single open book, dark wooden table, atmospheric haze` | moody, contemplative |
| 音乐节 | `abstract layered wave forms, chromatic aberration, retro feel` | neon pink, electric blue, acid green |
| 体育/运动会 | `motion trails of sprinter mid-stride, diagonal composition, grunge texture` | orange, electric blue |
| 公益/环保（手绘）| `hand-drawn ink line art, watercolor washes, deckled paper edges, vintage broadside` | dawn pink, gold, storm grey |
| 餐饮新品 | `single plated dish, dramatic side lighting, steam through bokeh background` | 暗调 + 暖光 |

**海报命脉**：主视觉 + 大量负空间 + 强情绪。

---

### 4. 社交媒体（7 种平台）

| 平台/场景 | 核心关键词 | 比例 |
|-----------|-----------|------|
| 公众号头图·城市夜景 | `editorial cityscape, illuminated skyline, long-exposure, left 2/3 subject, right 1/3 sky` | 2.4:1 |
| 公众号头图·生活方式 | `sunlit wooden cabin, misty mountain valley, desaturated earthy palette` | 2.4:1 |
| 朋友圈九宫格 | `overhead flat-lay, weekend brunch, linen tablecloth, natural window light` | 1:1 |
| 小红书·治愈 | `hands holding matcha latte, sunlit windowsill, shallow depth of field, cream + sage green` | 3:4 |
| 抖音竖屏封面（手绘）| `hand-drawn portrait, bold ink line art, flat color fills, cybernetic patterns, paper texture, ink bleeds` | 9:16 |
| B 站横屏封面 | `cinematic still, neon-lit cyberpunk alley, leading lines, teal + magenta grading` | 16:9 |
| 节日祝福图 | `plum blossoms, traditional ink-wash, gold foil accents, warm beige + crimson` | 9:16 |

**社交媒体关键**：有"人味儿"或"场景感"，不要过度设计。

---

### 5. 电商主图（8 种模板）

| 模板 | 核心关键词 | 格式 |
|------|-----------|------|
| 3C 数码 | `premium product photo, pure white background, soft studio lighting, subtle reflection` | PNG 透明 |
| 服饰白底 | `folded cashmere sweater, pure white seamless, soft overhead lighting, crisp focus` | PNG 透明 |
| 食品特写（手绘感）| `artisan chocolate truffle, hand-painted paper-textured surface, dramatic side lighting, brush strokes, film grain` | 3:4, HD |
| 美妆平铺 | `flat-lay, luxury skincare, marble surface, flower petals, water droplets` | 1:1 |
| 家居场景 | `designer ceramic vase, sunlit Scandinavian living room, linen curtains, soft beige + cream` | 3:4 |
| 节日礼盒 | `deep green gift box, gold silk ribbon, marble surface, bokeh fairy lights` | 3:4 |
| 限时秒杀 | `dynamic speed lines, glowing shopping cart, dark gradient, high-energy` | 4:1 |
| 详情页头图 | `low angle shot, dramatic lighting, premium material texture, dark gradient` | 3:4 |

**电商命脉**：主体清晰、色彩纯正、构图可加文字。

---

### 6. 头像（7 种类型）

| 类型 | 核心关键词 | 风格 |
|------|-----------|------|
| 商务男性（手绘）| `editorial fashion illustration, bold ink line art, watercolor washes, paper texture, ink bleed` | 编辑插画 |
| 商务女性 | `professional headshot, soft studio lighting, subtle rim light, blurred office background` | 摄影写实 |
| 创意职业 | `casual creative, curly hair, round glasses, natural daylight, plant bokeh, 50mm lens` | 自然生活 |
| Q 版卡通 | `chibi-style, large expressive eyes, oversized hoodie, soft pastel pink, kawaii` | 卡通 |
| 专业人士 | `white coat, kind trustworthy expression, soft clinical lighting, blurred hospital corridor` | 职业写实 |
| 节日头像 | `cute cartoon, red tangzhuang, gold embroidery, plum blossom pattern, festive` | 卡通 |
| 家庭/亲子 | `parent and child laughing, soft natural light, cozy living room, 35mm lens` | 温馨写实 |

**头像命脉**：主体清晰、表情自然、背景简洁、脸占画面 50%+。

---

### 7. Logo 底图（8 种行业）

| 行业 | 核心关键词 | 配色 |
|------|-----------|------|
| 餐饮 | `coffee bean morphing into leaf, abstract emblem, modern minimal` | forest green, warm copper |
| 科技初创（纸艺）| `hand-cut paper craft, layered geometric shapes, hand-torn paper edges, paper fiber texture` | midnight navy, electric cyan |
| 教育培训 | `stylized open book, glowing graduation cap, friendly yet professional` | warm yellow, navy blue |
| 医疗健康 | `heart shape intertwined with leaf, modern minimal` | mint green, warm coral |
| 文创/手作 | `hand-drawn bird in flight, ink-wash style, gold foil accents, organic` | warm beige, crimson |
| 宠物店 | `dog and cat in negative space, friendly approachable` | caramel, sage green |
| 运动/健身 | `dynamic arrow piercing through circle, high-energy bold` | charcoal, electric orange |
| 美业/美容 | `elegant abstract flower, three soft petals, feminine luxurious` | rose gold, blush pink |

**Logo 底图关键**：必须明确说 `no text, no letters, abstract emblem only`。

---

### 8. 贴纸/表情包（8 种模板）

| 模板 | 核心关键词 | 特色 |
|------|-----------|------|
| 萌系表情（手绘）| `hand-drawn kawaii, marker line art, watercolor fills, visible brush strokes, color bleeds` | 柴犬/熊猫/柯基 |
| 节日贴纸 | `chubby cartoon, traditional tang suit, gold ingots, plum blossoms` | 春节/圣诞 |
| 萌宠表情 | `head tilted, tongue out, big glossy eyes, photographic + illustration overlay` | 柴犬特写 |
| Emoji 风格 | `yellow emoji-style face, exaggerated expression, classic flat emoji art` | 微信聊天用 |
| 文艺短句配图 | `single dried flower, translucent glass vase, soft watercolor, muted earth tone` | 配文字给 Canva |
| 涂鸦风 | `hand-drawn doodle set, scattered cute icons, black ink line-art, subtle color fills` | 太阳/月亮/仙人掌 |
| 励志小语配图 | `tiny hiker reaching summit, triangular mountain, soft orange pink sky` | 山/日出/小人物 |
| IP 角色贴纸 | `brand mascot, cute cartoon avocado, straw hat, kawaii soft outlines` | 牛油果/梨/芒果 |

**贴纸命脉**：轮廓清晰 + 透明背景 + 单个主体 + 强情绪。

---

### 9. Banner / 长条广告（8 种模板）

| 模板 | 核心关键词 | 比例 |
|------|-----------|------|
| Web 顶部 banner | `abstract 3D shape, layered translucent glass panels, gradient white→lavender, left 2/3 empty` | 4:1 |
| App 启动屏 | `abstract gradient deep indigo→soft pink, glowing orb center-right, premium modern` | 9:16 |
| 邮件头图 | `overhead shot, wooden desk, laptop + coffee + plant, warm muted tones, left empty` | 4:1 |
| 公众号关注引导 | `warm gradient peach→cream, stylized hand holding smartphone, abstract decorative dots` | 4:1 |
| 招聘 banner | `abstract gradient purple→electric blue, team silhouette, dynamic light streaks, left half empty` | 4:1 |
| 展会/活动 | `overlapping translucent geometric shapes, dark charcoal, slight grain, dynamic diagonal` | 4:1 |
| 电商首页 banner | `vibrant pink→deep purple, floating shopping icons low opacity, glowing circular spotlight` | 4:1 |
| 横幅广告/户外 | `bold product silhouette, dramatic side lighting, motion blur, electric orange accent` | 4:1 |

**Banner 铁律**：主体永远放在右 1/3 或左 1/3，中间留白放标题。

---

## 四、通用负面提示词库（每条必加）

```
no text, no letters, no characters, no words, no numbers, no logo, no watermark
```

按场景补充：
```
头像/贴纸/logo：加 no background（要透明背景时）
PPT/海报/电商：加 no QR code, no screen content, no brand marks
logo 类：加 no cross, no medical symbols（避免模型画红十字等）
PPT 封面：加 no seal（避免画印章）
食物/产品：加 no plate, no hangers, no tags
```

---

## 五、迭代改稿标准指令

```
改色（不改变构图）：
"Keep the exact same composition, layout, and elements. Change the entire color palette to [新配色]. No text."

改风格（写实 → 扁平/手绘）：
"Convert this to [新风格]. Keep the same layout and color temperature. No text."

换主体（不改变风格和氛围）：
"Same style, same palette, same composition. Replace the main subject with [新主体]. No text."

派生内页（降低元素密度）：
"Same palette and style as the cover. Lower density, larger negative space, subtle elements only. No text."

同角色不同动作（贴纸系列）：
"Same character, same style, same outline. Change the pose to [新动作]. No text."
```

---

## 六、使用说明（给你的 AI 看）

你现在是一个 AI 图像生成 prompt 专家。上面这份框架来自 75 条实战验证的 prompt 模板，覆盖 9 个办公场景。

当你收到一个出图需求时，按以下流程：

1. **确定场景** → 查找上面对应的场景速查表
2. **选风格关键词** → 从表中提取核心关键词
3. **确定构图/留白** → 主体放在左侧 1/3 还是右侧 1/3？留白在上面还是下面？
4. **加入抗 AI 关键词** → 从工具箱中选 2-3 个（hand-painted / paper grain / ink bleeds / paper craft 等）
5. **补上负面提示** → `no text, no letters, no characters`
6. **输出完整 prompt** → 按七要素骨架输出一句完整英文 prompt

现在请用这个框架，帮我生成图片。我会告诉你场景和需求。
