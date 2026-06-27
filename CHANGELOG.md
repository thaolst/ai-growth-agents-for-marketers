# Changelog

All notable changes to this project are documented here.

## [1.2.0] - 2026-06-27

### Added
- **New skill: social-listening** (#20) — Monitor social platforms for brand mentions, competitor activity, and growth trends
- **SKILL-TEMPLATE.md** — reusable template to scaffold new skills faster

### Changed
- **Makefile** — added `make scaffold NAME=x DESC="y"` target for quick skill creation
- **skills.json** — updated to v1.2.0 with new skill entry

## [1.1.0] - 2026-06-01

### Added
- **5 new Agent Skills** (15 total): `fintech-campaign-designer`, `voucher-mechanic-designer`, `retention-analyzer`, `churn-intervention`, `growth-mcp-connect`
- **Context system**: `.agents/product-marketing-context.md` — shared context read by all 15 skills (like Corey Haines 31k⭐ repo)
- **Data connector**: growth-mcp integration for live campaign data, cohort data, experiment data
- **Cross-referenced skills** with dependency map in skills/README.md
- **Growth metrics context**: `.agents/growth-metrics-context.md` for manual metric overrides

### Changed
- **All 10 existing skills** upgraded to v1.1 with context references + related skills cross-links
- **README** — added "What Makes This Different" table, context system section, data connector section
- **Skills table** — expanded from 10 to 15 skills with context column
- **skills/README.md** — full dependency map with cross-references visualization

### What differentiates us
- Dual format: Agent Skills + executable Python agents (unique vs Corey Haines, LeoYeAI, AgentKits)
- Fintech + SEA context (unique)
- Data connector via growth-mcp (unique)

## [1.0.0] - 2026-05-29

### Added
- **Star History chart** — visual star growth tracker in README
- **Discussions templates** — Q&A, Ideas & Suggestions, Share & Showcase templates for community onboarding
- **CONTRIBUTING.md** — enhanced with "Start from Discussions" section
- **Dependabot config** — auto-dependency updates for Python + GitHub Actions
- **GitHub Pages workflow** — auto-deploy website on push to main

### Changed
- **README** — added Contribute button, star-history badge, improved navigation
- **Navigator** — moved from beta to stable as default mode

### Fixed
- **README** — removed duplicate community section, consistent navigation

## [0.9.0] - 2026-05-28

### Added
- 10 Agent Skills for npx install (Agent Skills spec)
- DevContainer setup (one-click Codespaces)
- GitHub Pages landing page (docs/index.html)
- CI/CD pipeline (validate.yml) — markdown lint, Python syntax, agent structure check
- Issue templates: bug report, feature request, documentation, prompt improvement
- Pull request template
- FUNDING.yml
- SECURITY.md
- Makefile with setup/validate/run/lint targets
- Case studies: dormant reactivation, A/B test push notification

### Changed
- All Python agents: dual Anthropic + OpenAI support
- README: full bilingual (VI/EN), improved structure

## [0.5.0] - 2026-05-24

### Added
- 10 agents with full structure (README, prompt, example-output)
- Python implementations for 7 agents (04-10)
- No-code agents for 3 use cases (01, 02, 03, 06)
- Bilingual prompts (VI + EN)
- Real example outputs from actual campaigns

## [0.1.0] - 2026-05-20

### Added
- Initial release
- Core agent framework and structure
- First 5 agents
