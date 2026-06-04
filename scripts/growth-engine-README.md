# Growth Engine — GitHub Repo Development Agent

![version](https://img.shields.io/badge/version-1.0.0-4ade80?style=flat-square) ![type](https://img.shields.io/badge/type-agent-60a5fa?style=flat-square) [![← repo](https://img.shields.io/badge/←_back-repo-a78bfa?style=flat-square)](../README.md)

**Automated daily agent** for managing and growing Thảo's GitHub repos — with memory, roadmap, tracking, and social content suggestion.

Built for positioning as **Top 1 AI x Growth Marketing in SEA**.

## Flow

```
19:30 GitHub Actions → Suggest task via Telegram
      ↓
20:00 Thảo approves or suggests different task
      ↓
Execute → Push GitHub → Suggest social content
```

## Features

| Feature | Description |
|---------|-------------|
| 📊 **GitHub API** | Tracks real-time stars, forks, commits for both repos |
| 🧠 **Memory** | Logs all dev activity, avoids repeating topics |
| 🗺️ **Roadmap** | Weekly plan with auto-priority (agents > prompts) |
| 📝 **Content Suggester** | Auto-generates LinkedIn/Facebook/Threads hooks |
| 🎯 **SEA Target** | Tracks progress toward Top 1 AI x Growth in SEA (target: 100★) |

## Usage

```bash
# Daily suggest — scans repos, checks memory, proposes task
python3 scripts/growth-engine.py daily

# Execute approved task
python3 scripts/growth-engine.py execute agents "Build Campaign Monitor Agent"
```

### Automatic (GitHub Actions)

Runs daily at 19:30 GMT+7 via `content-suggest.yml` — suggests 1 task + content hook via Telegram.

## How It Decides

1. **Weekly roadmap** — predefined tasks for current week
2. **Priority weights** — agents repo (weight 3) > prompts repo (weight 2)
3. **Recent memory** — avoids repeating recent work
4. **Performance** — prioritizes topics that perform well on social

## Target

**Top 1 AI x Growth Marketing GitHub repo in SEA (2026 Q3)**

| Milestone | Status |
|-----------|--------|
| 10★ — Early adopters | ✅ Prompts at 8★ |
| 50★ — Regional recognition | 🔄 In progress |
| 100★ — Top 1 SEA | 🎯 Target |
| 500★ — Global awareness | 🚀 Future |

## Tech

- Python 3.11+
- GitHub REST API (public, no auth needed)
- Telegram Bot API
- Not dependencies beyond standard library + `requests`
