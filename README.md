<img src="./images/banner.svg" alt="AI Growth Agents for Marketers" width="100%"/>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/thaolst/ai-growth-agents-for-marketers?color=60a5fa&style=flat-square" alt="license" /></a>
  <img src="https://img.shields.io/github/last-commit/thaolst/ai-growth-agents-for-marketers?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/ai-growth-agents-for-marketers?style=flat-square&color=facc15&logo=github" alt="stars" />
  <img src="https://img.shields.io/badge/language-VI%20%2B%20EN-blue?style=flat-square" alt="language" />
  <img src="https://img.shields.io/badge/free-forever-brightgreen?style=flat-square" alt="free" />
  <img src="https://img.shields.io/badge/providers-Anthropic%20%7C%20OpenAI-8A2BE2?style=flat-square" alt="providers" />
  <a href="https://codespaces.new/thaolst/ai-growth-agents-for-marketers"><img src="https://img.shields.io/badge/Open%20in-Codespaces-181717?style=flat-square&logo=github" alt="open in codespaces" /></a>
</p>


<p align="center">
  <a href="https://www.linkedin.com/in/thaolst/"><img src="https://img.shields.io/badge/LinkedIn-Lê%20Song%20Tiên%20Thảo-blue?style=flat-square&logo=linkedin" alt="LinkedIn" /></a>
  <img src="https://img.shields.io/badge/built%20from-real%20campaigns-ff6b6b?style=flat-square" alt="built from real campaigns" />
  <img src="https://img.shields.io/badge/fintech-SEA-00d4b4?style=flat-square" alt="fintech SEA" />
</p>


## Cài đặt qua Agent Skills

```bash
npx skills add thaolst/ai-growth-agents-for-marketers
```

Hoạt động với Claude Code, OpenAI Codex, Cursor, và mọi agent hỗ trợ Agent Skills spec.

---

> Không phải template. Không phải lý thuyết. Agent thật, chạy được, từ campaign thực tế.
> Not templates. Not theory. Real agents, actually run, from live campaigns.

# Tiếng Việt

## AI Growth Agents for Marketers

Mình dùng AI agent trong công việc growth marketing hàng ngày — để viết brief, phân tích A/B test, lên campaign plan, đề xuất mechanic voucher. Repo này là những gì thực sự chạy được, không phải những gì trông hay trên slide.

### Kết quả thực tế

| Công việc | Trước | Sau |
|---|-|-|
| Viết campaign brief | 3 tiếng | 20 phút |
| Phân tích A/B test | 3 tiếng | 15 phút |
| Báo cáo growth hàng tuần | 4 tiếng | Tự động |
| Đề xuất voucher mechanic | Cảm tính | 10 phút |

### Có gì trong này

| Agent | Làm gì |
|-|--|
| [Campaign Brief Agent](./02-your-first-campaign-agent/) | 5 input → brief hoàn chỉnh |
| [Tool Use — Không code](./03-tool-use-no-code/) | Agent đọc file, tìm kiếm, tổng hợp |
| [Tool Use — Python](./04-tool-use-python/) | Agent tự kéo data, không cần can thiệp |
| [Multi-Agent Workflow](./05-multi-agent-workflow/) | Nhiều agent phối hợp trong một pipeline |
| [Agentic RAG](./06-agentic-rag/) | Agent đọc toàn bộ campaign cũ, trả lời câu hỏi |
| [Planning Agent](./07-planning-agent/) | Input target → output toàn bộ plan |
| [A/B Test Analyzer](./08-ab-test-analyzer/) | Tự phát hiện winner, tự đề xuất bước tiếp |
| [MEU Planning Agent](./09-meu-planning-agent/) | Làm ngược từ growth target ra campaign |
| [Agents in Production](./10-agents-in-production/) | Deploy và chạy agent thật, không chỉ demo |
| [Case Studies](./case-studies/) | Kết quả thực tế từ campaign đã chạy, số liệu ẩn danh |

### Agent Skills (dùng với Claude Code, Cursor, Codex)

```bash
# Cài tất cả skills
npx skills add thaolst/ai-growth-agents-for-marketers

# Hoặc cài skill cụ thể
npx skills add thaolst/ai-growth-agents-for-marketers/skills/campaign-brief
```

| Skill | Agent | Làm gì |
|-|-|-|
| `campaign-brief` | [02](./02-your-first-campaign-agent/) | Viết campaign brief hoàn chỉnh |
| `campaign-synthesis` | [03](./03-tool-use-no-code/) | Tổng hợp nhiều file campaign |
| `automation-scripter` | [04](./04-tool-use-python/) | Tự động code Python cho marketer |
| `multi-agent-research` | [05](./05-multi-agent-workflow/) | Research → Planning pipeline |
| `rag-knowledge-base` | [06](./06-agentic-rag/) | Hỏi đáp từ kho tài liệu campaign |
| `campaign-planning` | [07](./07-planning-agent/) | Lên plan campaign từ target |
| `ab-test-analyzer` | [08](./08-ab-test-analyzer/) | Phân tích A/B test |
| `meu-planning` | [09](./09-meu-planning-agent/) | Làm ngược từ MEU target |
| `agent-pre-deploy-review` | [10](./10-agents-in-production/) | Review agent trước khi deploy |
| `ai-agent-consultant` | [01](./01-what-is-ai-agent/) | Tư vấn chọn agent phù hợp |

### Cấu trúc mỗi agent

```
📁 tên-agent/
├── README.md          ← Mình dùng nó như thế nào
├── prompt.md          ← Prompt thực tế, copy và dùng
├── agent.py           ← Python (một số agent)
└── example-output.md  ← Output thật từ campaign thật
```

### Bắt đầu

**Không code — dùng ngay:**
```
Mở Claude.ai → paste prompt từ bất kỳ thư mục nào
```

**Có Python:**
```bash
git clone https://github.com/thaolst/ai-growth-agents-for-marketers
cd ai-growth-agents-for-marketers
pip install -r requirements.txt
cp .env.example .env
```

Mỗi agent Python có `requirements.txt` riêng nếu bạn chỉ muốn cài agent cụ thể:
```bash
cd 08-ab-test-analyzer
pip install -r requirements.txt
```

**One-click setup với Codespaces:**
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-181717?style=flat-square&logo=github)](https://codespaces.new/thaolst/ai-growth-agents-for-marketers)
Mở repo trong GitHub Codespaces — môi trường Python đã cấu hình sẵn, chỉ cần thêm API key.

**Makefile helper:**
```bash
make setup        # Cài dependencies + copy .env.example
make validate     # Kiểm tra toàn bộ cấu trúc repo
make run AGENT=08-ab-test-analyzer  # Chạy agent cụ thể
make list         # Xem danh sách agent
make clean        # Dọn __pycache__ và file tạm
```

**Chọn provider:** Mặc định dùng Anthropic Claude. Set `AI_PROVIDER=openai` trong `.env` để dùng OpenAI GPT.

| Biến | Mặc định | Ghi chú |
|------|----------|---------|
| `AI_PROVIDER` | `anthropic` | `anthropic` hoặc `openai` |
| `ANTHROPIC_API_KEY` | — | Lấy tại console.anthropic.com |
| `OPENAI_API_KEY` | — | Chỉ cần nếu dùng OpenAI |
| `AI_MODEL` | (tự động) | Ghi đè model nếu muốn |

### Tác giả

**Lê Song Tiên Thảo**

Growth Marketer. Mình build agent, prompt, và workflow cho công việc growth thực tế — trong giới hạn thật của budget, channel, và segment.

[LinkedIn](https://www.linkedin.com/in/thaolst/) · [GitHub](https://github.com/thaolst) · [Substack](https://thaolst.substack.com/)

⭐ Star repo này nếu nó tiết kiệm cho bạn ít nhất 1 tiếng.

# English

## AI Growth Agents for Marketers

I use AI agents daily for growth marketing work — writing briefs, analyzing A/B tests, planning campaigns, recommending voucher mechanics. This repo is what actually runs, not what looks good on slides.

### Real results

| Task | Before | After |
|--|--|-|
| Campaign brief | 3 hours | 20 minutes |
| A/B test analysis | 3 hours | 15 minutes |
| Weekly growth report | 4 hours | Automated |
| Voucher recommendation | Gut feeling | 10 minutes |

### What's inside

| Agent | Does what |
|-|---|
| [Campaign Brief Agent](./02-your-first-campaign-agent/) | 5 inputs → complete brief |
| [Tool Use — No Code](./03-tool-use-no-code/) | Agent reads files, searches, summarizes |
| [Tool Use — Python](./04-tool-use-python/) | Agent pulls data automatically |
| [Multi-Agent Workflow](./05-multi-agent-workflow/) | Multiple agents running in one pipeline |
| [Agentic RAG](./06-agentic-rag/) | Agent reads all past campaigns, answers questions |
| [Planning Agent](./07-planning-agent/) | Input target → full campaign plan |
| [A/B Test Analyzer](./08-ab-test-analyzer/) | Auto-detects winner, recommends next steps |
| [MEU Planning Agent](./09-meu-planning-agent/) | Works backward from growth target to campaign |
| [Agents in Production](./10-agents-in-production/) | Deploy and run real agents, not just demos |
| [Case Studies](./case-studies/) | Real results from live campaigns, numbers anonymized |

### Author

**Lê Song Tiên Thảo**

Growth Marketer building agents, prompts, and workflows for real growth work — within real constraints of budget, channel, and segment behavior.

[LinkedIn](https://www.linkedin.com/in/thaolst/) · [GitHub](https://github.com/thaolst) · [Substack](https://thaolst.substack.com/)

### Provider support

All Python agents support both **Anthropic Claude** (default) and **OpenAI GPT**.
Set `AI_PROVIDER=openai` in `.env` to switch, or override the model with `AI_MODEL`.

⭐ Star this if it saves you at least 1 hour.
