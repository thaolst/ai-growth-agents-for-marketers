# Growth Marketing Skills — Agent Skills for Growth Marketers

A collection of **15 AI agent skills** for growth marketing — built from real fintech campaigns.
Works with Claude Code, OpenAI Codex, Cursor, and any agent that supports the Agent Skills spec.

## Dependency Map

Skills cross-reference each other. The `.agents/product-marketing-context.md` file is the foundation —
every skill checks it first before asking questions.

```
.product-marketing-context.md (read by ALL skills first)
│
├── fintech-campaign-designer (fintech-specific campaign design)
│   ├── campaign-brief (write detailed brief)
│   ├── campaign-planning (monthly/quarterly plan)
│   └── meu-planning (reverse-plan from MEU target)
│
├── voucher-mechanic-designer (design + optimize mechanics)
│   ├── campaign-brief
│   ├── ab-test-analyzer
│   └── fintech-campaign-designer
│
├── retention-analyzer (diagnose retention)
│   ├── churn-intervention (design save offers)
│   └── growth-mcp-connect (pull real data)
│
├── campaign-synthesis (synthesize multiple docs)
│   └── multi-agent-research (2-agent pipeline)
│
├── ai-agent-consultant (choose right agent type)
│   ├── automation-scripter (Python scripts)
│   ├── campaign-synthesis
│   └── agent-pre-deploy-review (review before deploy)
│
├── rag-knowledge-base (no-code RAG from campaign docs)
│
└── growth-mcp-connect (DATA CONNECTOR — connect to growth-mcp for live metrics)
    ├── campaign-brief
    ├── ab-test-analyzer
    ├── meu-planning
    ├── retention-analyzer
    └── churn-intervention
```

## Skills Available (15 total)

### Fintech Campaign Design
| Skill | Description | Code? |
|-------|-------------|-------|
| [fintech-campaign-designer](./fintech-campaign-designer/) | Full fintech campaign design (SEA-focused) | ❌ |
| [campaign-brief](./campaign-brief/) | Write campaign brief from 5 inputs | ❌ |
| [campaign-planning](./campaign-planning/) | Monthly/quarterly campaign plan | ❌ |
| [meu-planning](./meu-planning/) | Reverse-plan from MEU target | ❌ |

### Voucher & Mechanics
| Skill | Description | Code? |
|-------|-------------|-------|
| [voucher-mechanic-designer](./voucher-mechanic-designer/) | Design/optimize voucher mechanics | ❌ |

### Retention & Churn
| Skill | Description | Code? |
|-------|-------------|-------|
| [retention-analyzer](./retention-analyzer/) | Diagnose retention drops, recommend interventions | ❌ |
| [churn-intervention](./churn-intervention/) | Design save offers and winback campaigns | ❌ |
| [ab-test-analyzer](./ab-test-analyzer/) | Analyze A/B test results | ❌ |

### Analysis & Research
| Skill | Description | Code? |
|-------|-------------|-------|
| [campaign-synthesis](./campaign-synthesis/) | Synthesize multiple campaign documents | ❌ |
| [multi-agent-research](./multi-agent-research/) | 2-agent research-to-planning pipeline | ❌ |
| [rag-knowledge-base](./rag-knowledge-base/) | No-code RAG from campaign documents | ❌ |

### Agent Building
| Skill | Description | Code? |
|-------|-------------|-------|
| [ai-agent-consultant](./ai-agent-consultant/) | Choose the right AI agent type | ❌ |
| [automation-scripter](./automation-scripter/) | Generate Python scripts for repetitive tasks | 🐍 |
| [agent-pre-deploy-review](./agent-pre-deploy-review/) | Review agent before real deployment | ❌ |

### Data Connectors
| Skill | Description | Code? |
|-------|-------------|-------|
| [growth-mcp-connect](./growth-mcp-connect/) | **Connect to growth-mcp for live campaign data** | 🐍 |

## How the Context System Works

```
.agents/
├── product-marketing-context.md   ← Fill this once. All 15 skills read it.
└── growth-metrics-context.md      ← Optional. Manual metric overrides.
```

Every skill automatically checks these files before asking you questions.
Describe your product and metrics once — skills use them forever.

## Install

```bash
# Install all skills
npx skills add thaolst/ai-growth-agents-for-marketers

# Install specific skills
npx skills add thaolst/ai-growth-agents-for-marketers --skill campaign-brief ab-test-analyzer

# List available skills
npx skills add thaolst/ai-growth-agents-for-marketers --list
```

## What Makes These Skills Different

- **From real fintech campaigns** — not theory, not templates, from actual growth work at MoMo (40M+ users)
- **Southeast Asia focused** — Vietnam, Indonesia, Philippines, Thailand contexts built in
- **Dual format** — Skills + Python agents (run `make run AGENT=XX` for executable code)
- **Data connector** — growth-mcp MCP server pulls real metrics instead of guesswork
- **Bilingual** — full Vietnamese + English

# English

A collection of 15 AI agent skills for growth marketing, built from real fintech campaigns in Southeast Asia.

Works with Claude Code, OpenAI Codex, Cursor, and any agent supporting the Agent Skills spec.

Install: `npx skills add thaolst/ai-growth-agents-for-marketers`
