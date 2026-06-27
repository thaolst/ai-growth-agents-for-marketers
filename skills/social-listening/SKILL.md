---
name: social-listening
description: >
  Monitor social platforms for brand mentions, competitor activity, and growth
  marketing trends. Use when the user wants to track brand sentiment, spot
  market trends, or research competitors. Combines manual research workflows
  with API-based automation where available.
metadata:
  author: thaolst
  version: "1.0"
  license: MIT
  related_skills:
    - campaign-brief
    - campaign-planning
    - ai-agent-consultant
---

# Social Listening for Growth Marketers

> Checks `.agents/product-marketing-context.md` for brand keywords.
> Checks `.agents/growth-metrics-context.md` for baseline metrics.

## One-Liner

Track what people say about your brand, competitors, and industry on social platforms — use signal to inform campaign strategy.

## How Social Listening Works

Social listening requires API access from each platform for automation.
Without APIs, you can still do **manual structured research** — systematic,
documented searches instead of random scrolling.

| Method | Needs | Best For |
|--------|-------|----------|
| **Manual research** | Browser + search | Quick checks, small teams getting started |
| **API-based** | Platform API keys + app review | Ongoing monitoring, scale |
| **Third-party tools** | Budget ($200–500/mo) | Cross-platform dashboards |

This skill covers **manual research** (anyone can do it) and outlines
what's needed to automate each platform.

## Platform Access Guide

| Platform | Manual Research | API Automation |
|----------|----------------|----------------|
| **LinkedIn** | Search by keyword, filter by date/post type | LinkedIn Marketing API (restricted, company page only) |
| **X / Twitter** | Advanced search: `brand keyword -filter:replies` | X API Basic ($100/mo) or Pro ($200/mo) |
| **Reddit** | Site search: `site:reddit.com/r/subreddit "keyword"` | Reddit API (free, OAuth, rate-limited) |
| **Facebook** | Platform search + public group browsing | Graph API (requires app review + business verification) |
| **Google News / Blog search** | Google Alerts (free) | Google News RSS API (limited) |

## When to Use This Skill

- Before a campaign launch — check sentiment and competitor activity
- After a campaign — measure earned conversation volume
- Weekly brand health check
- Competitor intelligence — what are competitors launching?

## Analysis Matrix

| Signal | What It Means | Action |
|--------|---------------|--------|
| 👎 Negative sentiment spike | Possible campaign fatigue or product issue | Investigate → pause or adjust campaign |
| 👍 Positive organic mention | Campaign is resonating | Amplify — boost with paid, repost |
| 🔄 Competitor launch | Market positioning shift | Analyze differentiation, adjust messaging |
| 💬 Recurring user question | Unmet need or feature gap | Create content, explore product opportunity |
| 📈 Trend keyword rise | Emerging market topic | Ride the trend — content or campaign |

## Manual Research Workflow

1. **Identify platforms** — pick 2-3 where your audience is most active
2. **Search systematically** — same keywords, same filters, same time weekly
3. **Log signals** — save findings in a shared doc (not just in your head)
4. **Classify by analysis matrix** — negative? positive? trend? question?
5. **Decide action** — each signal → one action (pause, amplify, pivot, create)

## Monitoring Cadence

| Frequency | Activity |
|-----------|----------|
| **Daily** | Quick scan — brand mentions, campaign hashtags, competitor posts (5 min) |
| **Weekly** | Deep scan — 5-10 posts per platform, sentiment trend (20 min) |
| **Monthly** | Report — key signals, action items, content opportunities |

## Checklist

- [ ] Identify 3-5 brand keywords to track
- [ ] Identify top 2 competitors
- [ ] Pick 2-3 platforms to monitor
- [ ] Understand API requirements if automating
- [ ] Set monitoring cadence (daily scan + weekly deep)
- [ ] Log signals in shared doc
- [ ] Connect signals to campaign decisions

## Related Skills

- [campaign-brief](../campaign-brief/) — write campaign brief informed by social signals
- [campaign-planning](../campaign-planning/) — build campaign plan around trend timing
- [ai-agent-consultant](../ai-agent-consultant/) — choose the right agent to automate listening
