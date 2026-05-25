# Setup

Có hai cách dùng repo này tùy mức độ muốn tự động hóa.

**Không code — bắt đầu từ đây:**

Chỉ cần tài khoản [Claude.ai](https://claude.ai). Mở Claude, paste prompt từ bất kỳ folder nào, dùng được ngay.

**Python — khi muốn agent tự chạy:**

Cần Python 3.9+ và Anthropic API key. Lấy API key miễn phí tại [console.anthropic.com](https://console.anthropic.com).

```bash
git clone https://github.com/thaolst/ai-growth-agents-for-marketers
cd ai-growth-agents-for-marketers
pip install -r requirements.txt
cp .env.example .env
```

Mở file `.env`, dán API key vào dòng `ANTHROPIC_API_KEY=`.

Kiểm tra:
```bash
python -c "import anthropic; print('OK')"
```

Chưa bao giờ dùng Terminal? Bắt đầu với prompt thuần trước. Quay lại phần Python khi cần.

# English

Two ways to use this repo depending on how much you want to automate.

**No code — start here:**

Just a [Claude.ai](https://claude.ai) account. Open Claude, paste any prompt from any folder, use immediately.

**Python — when you want agents to run automatically:**

Need Python 3.9+ and an Anthropic API key. Get a free key at [console.anthropic.com](https://console.anthropic.com).

```bash
git clone https://github.com/thaolst/ai-growth-agents-for-marketers
cd ai-growth-agents-for-marketers
pip install -r requirements.txt
cp .env.example .env
```

Open `.env`, paste your API key on the `ANTHROPIC_API_KEY=` line.

Verify:
```bash
python -c "import anthropic; print('OK')"
```

Never used Terminal before? Start with the no-code prompts first. Come back to Python when you need automation.
