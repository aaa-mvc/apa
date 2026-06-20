# 安装与配置

## 1. 安装依赖

skill 只用到一个第三方包：`python-dotenv`（用于读取 `.env`）。

```bash
cd /path/to/apa
pip3 install -r requirements.txt
```

> macOS 自带 Python 3，`pip3` 即可。如果没有 `python3`，先装一个。

## 2. 填配置

编辑本目录下的 `.env`（不是 `.env.example`）：

```bash
cp .env.example .env       # 第一次：先复制一份
$EDITOR .env               # 编辑
```

需要填三项：

```ini
AI_API_BASE_URL=https://YOUR-API-HOST/v1   # OpenAI 兼容协议入口
AI_API_KEY=YOUR_API_KEY                    # 你的 key
AI_MODEL=gpt-image-2                        # 模型名
```

`.env` 已经在 `.gitignore` 里，不会被误提交。

## 3. 验证

```bash
./bin/gpt-image preset
```

能看到预设列表 = 配置通了。

## 4. 第一次生图

```bash
./bin/gpt-image generate \
    --prompt "A modern minimalist PPT cover, deep blue gradient" \
    --preset ppt_cover_169
```

成功的话图会落在 `workspace/`，并写一行到 `workspace/history.jsonl`。

## 配置优先级

`lib/api.py` 读取顺序：

1. 调用 `GPTImageClient(base_url=..., api_key=..., model=...)` 时显式传入的参数
2. `.env` 文件（python-dotenv，`override=False`，不覆盖已存在的环境变量）
3. 当前 shell 的环境变量 `AI_API_BASE_URL` / `AI_API_KEY` / `AI_MODEL`
4. 内置默认模型名 `gpt-image-2`

所以在 CI / 容器里也能用 `export AI_API_KEY=...` 覆盖 `.env`。
