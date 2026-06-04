<img src="./images/banner.svg" alt="AI Growth Agents for Marketers" width="100%"/>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/thaolst/ai-growth-agents-for-marketers?color=60a5fa&style=flat-square" alt="license" /></a>
  <img src="https://img.shields.io/github/last-commit/thaolst/ai-growth-agents-for-marketers?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/ai-growth-agents-for-marketers?style=flat-square&color=facc15&logo=github" alt="stars" />
  <img src="https://img.shields.io/badge/language-VI%20%2B%20EN-blue?style=flat-square" alt="language VI + EN" />
  <img src="https://img.shields.io/badge/free-forever-brightgreen?style=flat-square" alt="free forever" />
  <img src="https://img.shields.io/badge/providers-Anthropic%20%7C%20OpenAI-8A2BE2?style=flat-square" alt="providers: Anthropic and OpenAI" />
  <a href="https://codespaces.new/thaolst/ai-growth-agents-for-marketers"><img src="https://img.shields.io/badge/Open%20in-Codespaces-181717?style=flat-square&logo=github" alt="open in GitHub Codespaces" /></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/thaolst/"><img src="https://img.shields.io/badge/LinkedIn-L%C3%AA%20Song%20Ti%C3%AAn%20Th%E1%BA%A3o-blue?style=flat-square&logo=linkedin" alt="LinkedIn - Le Song Tien Thao" /></a>
  <img src="https://img.shields.io/badge/built%20from-real%20campaigns-ff6b6b?style=flat-square" alt="built from real campaigns" />
  <img src="https://img.shields.io/badge/fintech-SEA-00d4b4?style=flat-square" alt="fintech Southeast Asia" />
  <img src="https://img.shields.io/badge/website-visit-8b5cf6?style=flat-square&logo=github-pages" alt="website" />
</p>

<p align="center">
  <a href="https://thaolst.github.io/ai-growth-agents-for-marketers"><strong>🌐 Website</strong></a> ·
  <a href="https://github.com/thaolst/ai-growth-agents-for-marketers/discussions"><strong>💬 Discussions</strong></a> ·
  <a href="./CONTRIBUTING.md"><strong>📝 Contribute</strong></a> ·
  <a href="./CHANGELOG.md"><strong>📋 Changelog</strong></a>
</p>

<p align="center">
  <a href="https://star-history.com/#thaolst/ai-growth-agents-for-marketers&Date"><img src="https://api.star-history.com/svg?repos=thaolst/ai-growth-agents-for-marketers&type=Date" width="450" alt="Star History" /></a>
</p>

<!--
Keywords: AI agents for growth marketing, marketing automation prompts, AI marketing agents, growth marketing AI tools, fintech marketing prompts, campaign brief AI, A/B test analysis AI, marketing agent prompts, Vietnamese AI marketing, Southeast Asia fintech marketing
-->

## Cài đặt qua Agent Skills

```bash
npx skills add thaolst/ai-growth-agents-for-marketers
```

Hoạt động với Claude Code, OpenAI Codex, Cursor, và mọi agent hỗ trợ Agent Skills spec.

> Không phải template. Không phải lý thuyết. Agent thật, chạy được, từ campaign thực tế.
> Not templates. Not theory. Real agents, actually run, from live campaigns.

# Tiếng Việt

## AI Growth Agents for Marketers

Mình dùng AI agent trong công việc growth marketing hàng ngày - để viết brief, phân tích A/B test, lên campaign plan, đề xuất mechanic voucher. Repo này là những gì thực sự chạy được, không phải những gì trông hay trên slide.

### Kết quả thực tế

| Công việc | Trước | Sau |
|----------|-------|-----|
| Viết campaign brief | 3 tiếng | 20 phút |
| Phân tích A/B test | 3 tiếng | 15 phút |
| Báo cáo growth hàng tuần | 4 tiếng | Tự động |
| Đề xuất voucher mechanic | Cảm tính | 10 phút |

### Ai nên dùng

- Growth marketer muốn tự động hóa công việc lặp lại
- Marketing manager cần brief / plan / report nhanh
- Founder / solo marketer làm nhiều việc một lúc
- Bất kỳ ai làm fintech, e-commerce, super app ở Đông Nam Á

### Có gì trong này

| Agent | Làm gì | Cần code? |
|-------|--------|-----------|
| [💡 AI Agent Consultant](./01-what-is-ai-agent/) | Tư vấn chọn agent phù hợp | ❌ |
| [📋 Campaign Brief Agent](./02-your-first-campaign-agent/) | 5 input → brief hoàn chỉnh | ❌ |
| [🔍 Campaign Synthesis](./03-tool-use-no-code/) | Tổng hợp nhiều file campaign | ❌ |
| [⚙️ Automation Scripter](./04-tool-use-python/) | Tự viết Python script | 🐍 |
| [🔄 Multi-Agent Pipeline](./05-multi-agent-workflow/) | Research → Planning | 🐍 |
| [📚 Agentic RAG](./06-agentic-rag/) | Hỏi đáp từ campaign history | ❌ |
| [🎯 Planning Agent](./07-planning-agent/) | Target → Campaign plan | 🐍 |
| [📊 A/B Test Analyzer](./08-ab-test-analyzer/) | Phân tích + đề xuất | 🐍 |
| [📈 MEU Planning](./09-meu-planning-agent/) | MEU target → Campaign plan | 🐍 |
| [🚀 Production Review](./10-agents-in-production/) | Review agent trước deploy | 🐍 |
| [📖 Case Studies](./case-studies/) | Kết quả thực tế, ẩn danh | - |

### Bắt đầu

**Không code - 1 phút:**
```bash
# Mở Claude.ai → paste prompt từ bất kỳ folder 01, 02, 03, 06
```

**Có Python - 2 phút:**
```bash
git clone https://github.com/thaolst/ai-growth-agents-for-marketers
cd ai-growth-agents-for-marketers
make setup
# Edit .env → dán API key → make run AGENT=08-ab-test-analyzer
```

**One-click - 0 phút setup:**
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-181717?style=flat-square&logo=github)](https://codespaces.new/thaolst/ai-growth-agents-for-marketers)
Môi trường Python + extensions sẵn, chỉ cần thêm API key.

### Cấu trúc mỗi agent

```
📁 agent-name/
├── README.md          ← Dùng nó như thế nào
├── prompt.md          ← Prompt thật, copy-paste và dùng
├── agent.py           ← Python (nếu cần tự động chạy)
├── requirements.txt   ← Dependencies (nếu có Python)
└── example-output.md  ← Output thật từ campaign thật
```

### 🌟 Điều làm repo này khác biệt

| Không giống ai | Vì sao độc đáo |
|----------------|----------------|
| **MEU Planning agent** | Repo duy nhất có agent lập kế hoạch ngược từ MEU - phổ biến ở fintech SEA, không ai làm |
| **Python agents chạy thật** | Skills markdown + 7 Python agents executable - dual format |
| **Fintech + SEA context** | Không lý thuyết SaaS Mỹ. Campaign thật ở Việt Nam, Indonesia, Philippines |
| **Data connector** | growth-mcp MCP server → real metrics, không guesswork |
| **Context system** | Điền `.agents/product-marketing-context.md` một lần → 15 skills dùng chung |
| **Bilingual VI/EN** | Prompt và skills 100% song ngữ |

### Agent Skills (dùng với Claude Code, Cursor, Codex)

```bash
# Cài tất cả (15 skills)
npx skills add thaolst/ai-growth-agents-for-marketers

# Cài skill cụ thể
npx skills add thaolst/ai-growth-agents-for-marketers/skills/campaign-brief
```

| Skill | Agent | Mô tả | Context? |
|-------|-------|-------|----------|
| `ai-agent-consultant` | [01](./01-what-is-ai-agent/) | Tư vấn chọn agent phù hợp | ✅ |
| `campaign-brief` | [02](./02-your-first-campaign-agent/) | Viết campaign brief | ✅ |
| `campaign-synthesis` | [03](./03-tool-use-no-code/) | Tổng hợp campaign | ✅ |
| `automation-scripter` | [04](./04-tool-use-python/) | Tạo Python script | ✅ |
| `multi-agent-research` | [05](./05-multi-agent-workflow/) | Research→Plan pipeline | ✅ |
| `rag-knowledge-base` | [06](./06-agentic-rag/) | RAG knowledge base | ✅ |
| `campaign-planning` | [07](./07-planning-agent/) | Campaign planning | ✅ |
| `ab-test-analyzer` | [08](./08-ab-test-analyzer/) | A/B test analysis | ✅ |
| `meu-planning` | [09](./09-meu-planning-agent/) | MEU planning | ✅ |
| `agent-pre-deploy-review` | [10](./10-agents-in-production/) | Pre-deploy review | ✅ |
| `voucher-mechanic-designer` | - | Thiết kế mechanic voucher | ✅ |
| `fintech-campaign-designer` | - | Campaign design cho fintech | ✅ |
| `retention-analyzer` | - | Phân tích retention | ✅ |
| `churn-intervention` | - | Save offer + winback | ✅ |
| `growth-mcp-connect` | - | **Data connector** → real data | 🟢 |

> ✅ = Skill tự động đọc `.agents/product-marketing-context.md`
> 🟢 = Skill kết nối growth-mcp để lấy real-time data

### 💡 Hệ thống Context (mới)

```bash
.agents/
├── product-marketing-context.md   ← Điền 1 lần → 15 skills tự động dùng
└── growth-metrics-context.md      ← Tùy chọn: metric baseline thủ công
```

Cách này giống Corey Haines (31k⭐ marketing skills) nhưng fintech-focused + có Python agents.

### 🔌 Data Connector: growth-mcp (mới)

Kết nối growth-mcp để pull real metrics:

```bash
git clone https://github.com/thaolst/growth-mcp.git
cd growth-mcp && pip install -e .
```

Khi growth-mcp chạy, các skill sẽ tự động:
- Pull campaign performance trước khi viết brief
- Pull real cohort data trước khi phân tích retention
- Pull experiment data trước khi phân tích A/B test
- So sánh recommendation với campaign history thật

### Chọn provider

Mặc định dùng Anthropic Claude. Set `AI_PROVIDER=openai` trong `.env` để dùng OpenAI GPT.

```bash
# Mặc định (Anthropic)
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...

# Hoặc OpenAI
AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-...
```

| Biến | Mặc định | Ghi chú |
|------|----------|---------|
| `AI_PROVIDER` | `anthropic` | `anthropic` hoặc `openai` |
| `ANTHROPIC_API_KEY` | - | [console.anthropic.com](https://console.anthropic.com) |
| `OPENAI_API_KEY` | - | Chỉ cần nếu dùng OpenAI |
| `AI_MODEL` | (default) | Ghi đè model nếu muốn |

### Tham gia cộng đồng

- [💬 Discussions](https://github.com/thaolst/ai-growth-agents-for-marketers/discussions) - hỏi đáp, chia sẻ kinh nghiệm
- [🐛 Report bug](https://github.com/thaolst/ai-growth-agents-for-marketers/issues/new?template=bug_report.md) - prompt không hoạt động
- [💡 Suggest agent](https://github.com/thaolst/ai-growth-agents-for-marketers/issues/new?template=feature_request.md) - đề xuất agent mới
- [📝 Pull Request](./CONTRIBUTING.md) - đóng góp prompt/agent

### Tác giả

**Lê Song Tiên Thảo** - Growth Marketer @ MoMo (fintech, SEA)

Mình build agent, prompt, và workflow cho công việc growth thực tế - trong giới hạn thật của budget, channel, và segment behavior.

[LinkedIn](https://www.linkedin.com/in/thaolst/) · [GitHub](https://github.com/thaolst) · [Substack](https://thaolst.substack.com/) · [Website](https://thaolst.github.io/ai-growth-agents-for-marketers)

⭐ Star repo này nếu nó tiết kiệm cho bạn ít nhất 1 tiếng. ⭐

# English

## AI Growth Agents for Marketers

I use AI agents daily for growth marketing work - writing briefs, analyzing A/B tests, planning campaigns, recommending voucher mechanics. This repo is what actually runs, not what looks good on slides.

### Real results

| Task | Before | After |
|------|--------|-------|
| Campaign brief | 3 hours | 20 minutes |
| A/B test analysis | 3 hours | 15 minutes |
| Weekly growth report | 4 hours | Automated |
| Voucher recommendation | Gut feeling | 10 minutes |

### Who uses this

- Growth marketers who write the same brief structure every week and want that part automated
- Marketing managers running on tight timelines - brief, plan, report, repeat
- Founders doing growth alone without a team
- Anyone running campaigns in fintech, e-commerce, or super apps across SEA

### What's inside

| Agent | What it does | Code? | Context? |
|-------|-------------|-------|----------|
| [💡 AI Agent Consultant](./01-what-is-ai-agent/) | Choose the right agent type | ❌ | ✅ |
| [📋 Campaign Brief Agent](./02-your-first-campaign-agent/) | 5 inputs → complete brief | ❌ | ✅ |
| [🔍 Campaign Synthesis](./03-tool-use-no-code/) | Synthesize multiple files | ❌ | ✅ |
| [⚙️ Automation Scripter](./04-tool-use-python/) | Auto-generate Python scripts | 🐍 | ✅ |
| [🔄 Multi-Agent Pipeline](./05-multi-agent-workflow/) | Research → Planning | 🐍 | ✅ |
| [📚 Agentic RAG](./06-agentic-rag/) | Q&A from campaign history | ❌ | ✅ |
| [🎯 Planning Agent](./07-planning-agent/) | Target → full campaign plan | 🐍 | ✅ |
| [📊 A/B Test Analyzer](./08-ab-test-analyzer/) | Analyze + recommend | 🐍 | ✅ |
| [📈 MEU Planning](./09-meu-planning-agent/) | MEU target → campaigns | 🐍 | ✅ |
| [🚀 Production Review](./10-agents-in-production/) | Pre-deploy review | 🐍 | ✅ |
| [💰 Voucher Mechanic Designer](#) | Voucher/cashback design | ❌ | ✅ |
| [🏦 Fintech Campaign Designer](#) | SEA fintech campaign design | ❌ | ✅ |
| [📉 Retention Analyzer](#) | Cohort retention diagnosis | ❌ | ✅ |
| [🛑 Churn Intervention](#) | Save offers + winback | ❌ | ✅ |
| [🔌 growth-mcp Connect](#) | **Data connector** → live data | 🐍 | 🟢 |
| [📖 Case Studies](./case-studies/) | Anonymized real results | - | - |

> ✅ = Auto-reads `.agents/product-marketing-context.md` for shared context
> 🟢 = Connects to growth-mcp MCP server for real-time data

### 🎯 What Makes This Different

Unlike every other marketing agent repo (Corey Haines, LeoYeAI, AgentKits), this one:

| Unique | Why it matters |
|--------|---------------|
| **MEU Planning agent** | Only repo with MEU-backward campaign planning - common in SEA fintech, ignored everywhere else |
| **Dual format** | Skills + executable Python agents - not just markdown |
| **Fintech + SEA** | Real campaign context from Vietnam, Indonesia, Philippines |
| **Data connector** | growth-mcp MCP server → live metrics, not guesswork |
| **Context system** | Fill `.agents/product-marketing-context.md` once → 15 skills share it |
| **Bilingual VI/EN** | Full Vietnamese + English prompts and skills |

### 💡 Context System

```
.agents/
├── product-marketing-context.md   ← Fill once → 15 skills auto-use it
└── growth-metrics-context.md      ← Optional: manual metric overrides
```

Inspired by Corey Haines (31k⭐) but fintech-focused + with real Python agents.

### 🔌 Data Connector: growth-mcp

Connect [growth-mcp](https://github.com/thaolst/growth-mcp) for live campaign data:

```bash
git clone https://github.com/thaolst/growth-mcp.git
cd growth-mcp && pip install -e .
```

When connected, skills automatically:
- Pull campaign performance before writing briefs
- Pull real cohort data before retention analysis
- Pull experiment data before A/B test analysis
- Compare recommendations against real campaign history

### Quick start

**No code - 1 minute:**
```bash
# Open Claude.ai → paste any prompt from folders 01, 02, 03, 06
```

**Python - 2 minutes:**
```bash
git clone https://github.com/thaolst/ai-growth-agents-for-marketers
cd ai-growth-agents-for-marketers
make setup
# Edit .env → paste API key → make run AGENT=08-ab-test-analyzer
```

**One-click - 0 setup:**
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-181717?style=flat-square&logo=github)](https://codespaces.new/thaolst/ai-growth-agents-for-marketers)

### Provider support

All Python agents support both **Anthropic Claude** (default) and **OpenAI GPT**. Set `AI_PROVIDER=openai` in `.env` to switch, or override with `AI_MODEL`.

### Join the community

- [💬 Discussions](https://github.com/thaolst/ai-growth-agents-for-marketers/discussions) - Q&A, share experiences
- [🐛 Report bug](https://github.com/thaolst/ai-growth-agents-for-marketers/issues/new?template=bug_report.md) - prompt not working
- [💡 Suggest agent](https://github.com/thaolst/ai-growth-agents-for-marketers/issues/new?template=feature_request.md) - suggest a new agent
- [📝 Pull Request](./CONTRIBUTING.md) - contribute prompts/agents

### Author

**Lê Song Tiên Thảo (Tara)** - Growth Marketing Manager @ MoMo (fintech, SEA)

Building AI agents, prompts, and workflows for real growth work - within real constraints of budget, channel, and segment behavior.

[LinkedIn](https://www.linkedin.com/in/thaolst/) · [GitHub](https://github.com/thaolst) · [Substack](https://thaolst.substack.com/) · [Website](https://thaolst.github.io/ai-growth-agents-for-marketers)

⭐ Star this if it saves you at least 1 hour. ⭐
