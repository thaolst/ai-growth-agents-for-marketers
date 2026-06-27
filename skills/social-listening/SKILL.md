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

# Social Listening cho Growth Marketers

> Kiểm tra `.agents/product-marketing-context.md` để biết brand keywords.
> Kiểm tra `.agents/growth-metrics-context.md` để biết baseline metrics.

## Mục đích

Theo dõi những gì người dùng nói về brand, đối thủ, và ngành trên social platforms —
dùng tín hiệu đó để quyết định campaign strategy.

---

# Tiếng Việt

## Social Listening hoạt động thế nào?

Social Listening tự động cần API từ từng platform. Không có API, bạn vẫn có thể
**research thủ công có cấu trúc** — tìm kiếm có hệ thống, ghi chép có tổ chức.

| Phương pháp | Cần gì | Phù hợp |
|-------------|--------|---------|
| **Research thủ công** | Trình duyệt + search | Kiểm tra nhanh, team nhỏ mới bắt đầu |
| **API tự động** | API keys + app review từ platform | Theo dõi thường xuyên, scale |
| **Third-party tools** | Ngân sách $200–500/tháng | Dashboard đa nền tảng |

Skill này hướng dẫn **research thủ công** (ai cũng làm được) và nêu rõ
từng platform cần gì để tự động hóa.

## Hướng dẫn từng nền tảng

| Nền tảng | Research thủ công | API tự động |
|----------|------------------|-------------|
| **LinkedIn** | Search theo keyword, lọc theo ngày/loại bài | LinkedIn Marketing API (giới hạn, chỉ company page) |
| **X / Twitter** | Advanced search: `từ khoá -filter:replies` | X API Basic ($100/tháng) hoặc Pro ($200/tháng) |
| **Reddit** | Site search: `site:reddit.com/r/subreddit "từ khoá"` | Reddit API (miễn phí, OAuth, giới hạn tốc độ) |
| **Facebook** | Search platform + xem public group | Graph API (cần app review + business verification) |
| **Google News** | Google Alerts (miễn phí) | Google News RSS API (giới hạn) |

## Khi nào dùng skill này

- Trước khi launch campaign — check sentiment + hoạt động đối thủ
- Sau campaign — đo lường earned conversation volume
- Kiểm tra brand health hàng tuần
- Competitor intelligence — đối thủ đang làm gì mới

## Bảng phân tích tín hiệu

| Tín hiệu | Ý nghĩa | Hành động |
|----------|---------|-----------|
| 👎 Negative spike | Campaign fatigue hoặc product issue | Điều tra → tạm dừng hoặc điều chỉnh campaign |
| 👍 Positive organic mention | Campaign đang resonate | Amplify — boost paid, repost |
| 🔄 Competitor launch | Market positioning thay đổi | Phân tích differentiation, điều chỉnh messaging |
| 💬 Câu hỏi lặp lại | Unmet need hoặc feature gap | Tạo content, khám phá cơ hội product |
| 📈 Trend keyword tăng | Chủ đề mới nổi | Đi theo trend — content hoặc campaign |

## Quy trình research thủ công

1. **Chọn nền tảng** — chọn 2-3 nơi audience của bạn hoạt động nhiều nhất
2. **Search có hệ thống** — cùng keyword, cùng bộ lọc, cùng thời điểm mỗi tuần
3. **Ghi chép tín hiệu** — lưu vào shared doc, không chỉ trong đầu
4. **Phân loại** — dùng bảng phân tích ở trên: negative? positive? trend? question?
5. **Quyết định hành động** — mỗi tín hiệu → một hành động (pause, amplify, pivot, create)

## Tần suất monitoring

| Tần suất | Hoạt động |
|----------|-----------|
| **Hàng ngày** | Quick scan — brand mentions, campaign hashtags, bài đối thủ (5 phút) |
| **Hàng tuần** | Deep scan — 5-10 bài mỗi nền tảng, xu hướng sentiment (20 phút) |
| **Hàng tháng** | Report — tín hiệu chính, action items, cơ hội content |

## Checklist

- [ ] Xác định 3-5 brand keywords cần track
- [ ] Xác định top 2 đối thủ
- [ ] Chọn 2-3 nền tảng để monitor
- [ ] Hiểu rõ API requirements nếu muốn tự động hóa
- [ ] Set monitoring cadence (daily scan + weekly deep)
- [ ] Ghi chép tín hiệu vào shared doc
- [ ] Kết nối tín hiệu với quyết định campaign

---

# English

## Purpose

Track what people say about your brand, competitors, and industry on social
platforms — use signal to inform campaign strategy.

## How Social Listening Works

Social listening requires API access from each platform for automation.
Without APIs, you can still do **manual structured research** — systematic,
documented searches instead of random scrolling.

| Method | Needs | Best For |
|--------|-------|----------|
| **Manual research** | Browser + search | Quick checks, small teams getting started |
| **API-based** | Platform API keys + app review | Ongoing monitoring, scale |
| **Third-party tools** | Budget ($200–500/mo) | Cross-platform dashboards |

## Platform Access Guide

| Platform | Manual Research | API Automation |
|----------|----------------|----------------|
| **LinkedIn** | Search by keyword, filter by date/post type | LinkedIn Marketing API (restricted, company page only) |
| **X / Twitter** | Advanced search: `keyword -filter:replies` | X API Basic ($100/mo) or Pro ($200/mo) |
| **Reddit** | Site search: `site:reddit.com/r/subreddit "keyword"` | Reddit API (free, OAuth, rate-limited) |
| **Facebook** | Platform search + public group browsing | Graph API (requires app review + business verification) |
| **Google News / Blog search** | Google Alerts (free) | Google News RSS API (limited) |

## Signal Analysis Matrix

| Signal | Meaning | Action |
|--------|---------|--------|
| 👎 Negative sentiment spike | Possible campaign fatigue or product issue | Investigate → pause or adjust campaign |
| 👍 Positive organic mention | Campaign is resonating | Amplify — boost with paid, repost |
| 🔄 Competitor launch | Market positioning shift | Analyze differentiation, adjust messaging |
| 💬 Recurring user question | Unmet need or feature gap | Create content, explore product opportunity |
| 📈 Trend keyword rise | Emerging market topic | Ride the trend — content or campaign |

## Manual Research Workflow

1. **Pick platforms** — choose 2-3 where your audience is most active
2. **Search systematically** — same keywords, same filters, same time weekly
3. **Log signals** — save findings in a shared doc
4. **Classify** — negative? positive? trend? question?
5. **Decide action** — one signal → one action (pause, amplify, pivot, create)

## Monitoring Cadence

| Frequency | Activity |
|-----------|----------|
| **Daily** | Quick scan — brand mentions, campaign hashtags, competitor posts (5 min) |
| **Weekly** | Deep scan — 5-10 posts per platform, sentiment trend (20 min) |
| **Monthly** | Report — key signals, action items, content opportunities |

## Related Skills

- [campaign-brief](../campaign-brief/) — write campaign brief từ social signals
- [campaign-planning](../campaign-planning/) — build campaign plan theo trend timing
- [ai-agent-consultant](../ai-agent-consultant/) — chọn agent phù hợp để automate listening
