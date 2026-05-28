---
name: multi-agent-research
description: >
  Run multi-agent research-to-planning pipeline using two sequential agents.
  Use when the user has campaign data and needs a structured plan without code.
  Agent 1 (Research) analyzes campaign data and returns structured JSON insights.
  Agent 2 (Strategy) takes those insights and produces a complete campaign plan.
  Input: campaign data, target, budget, timeline.
  Output: research findings as JSON → executable campaign plan.
metadata:
  author: thaolst
  version: "1.0"
  license: MIT
---

# Multi-Agent Research & Planning Agent

Bạn hướng dẫn marketer chạy hai agent nối tiếp nhau — không cần code, chỉ cần hai cuộc trò chuyện riêng trong Claude.

## Workflow

### Bước 1 — Research Agent
Phân tích dữ liệu campaign, trả về JSON insight:
- Top performing mechanics
- Underperforming areas
- Segment insights
- Recommended focus (top 3)
- Data gaps

### Bước 2 — Strategy Agent
Nhận JSON từ Research Agent + input target/budget/timeline từ người dùng → viết campaign plan hoàn chỉnh.

## Input cần có

- Dữ liệu campaign (file, số liệu, báo cáo)
- Target cho campaign mới
- Budget
- Timeline

## Output format

### Research output (JSON)
Cấu trúc cố định gồm 5 field: top_performing_mechanics, underperforming_areas, segment_insights, recommended_focus, data_gaps.

### Strategy output (Campaign plan)
- Cụ thể, chi tiết
- Mỗi quyết định được giải thích dựa trên insight từ research
- Target, budget, timeline được điền từ input người dùng

## Nguyên tắc

- Research Agent chỉ trả về JSON — không giải thích, không commentary
- Strategy Agent không tự suy luận từ data gốc, chỉ dùng JSON từ research
- Người dùng copy-paste JSON giữa hai cuộc trò chuyện

---

# English

Guide marketers through running two sequential agents — no code, just two separate Claude conversations.

## Workflow

### Step 1 — Research Agent
Analyze campaign data, return JSON insights with 5 fields: top_performing_mechanics, underperforming_areas, segment_insights, recommended_focus, data_gaps.

### Step 2 — Strategy Agent
Take JSON from Research Agent + user's target/budget/timeline → write complete campaign plan.

## Input needed

- Campaign data (files, numbers, reports)
- New campaign target
- Budget
- Timeline

## Output format

### Research output (JSON)
Fixed 5-field structure.

### Strategy output (Campaign plan)
Specific, detailed. Every decision explained using research insights.

## Principles

- Research Agent returns only JSON
- Strategy Agent relies only on the JSON, not raw data
- User copy-pastes JSON between two conversations
