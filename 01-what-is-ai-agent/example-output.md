# Example output — Agent tư vấn chọn loại agent phù hợp

Input dùng để tạo output này:

> Mình muốn tự động hóa việc viết báo cáo campaign hàng tuần. Hiện tại mình mất 3-4 tiếng mỗi thứ Hai để tổng hợp số liệu từ nhiều nguồn, viết nhận xét, và gửi cho team. Mình có data từ dashboard nội bộ, không biết code.

**Loại agent phù hợp nhất: Analysis + Reporting Agent (no-code)**

Việc bạn mô tả có thể giải quyết ngay bằng prompt-based agent — không cần code. Quy trình: bạn copy số liệu từ dashboard, paste vào Claude cùng với prompt, agent phân tích và viết báo cáo hoàn chỉnh.

**Bắt đầu ngay hôm nay:**

Tạo prompt template với cấu trúc sau và lưu lại để dùng mỗi tuần:

```
Bạn là analyst cho team growth. Đây là số liệu tuần [X]:
[Paste số liệu]

Viết báo cáo tuần với:
- 3 điểm nổi bật nhất (tốt hoặc xấu)
- So sánh với tuần trước
- 2-3 đề xuất hành động cho tuần tới
- Format gọn, đọc trong 2 phút
```

Thời gian tiết kiệm ước tính: từ 3-4 tiếng xuống còn 30-45 phút.

**Để tự động hoàn toàn cần thêm:**

Python script kết nối API của dashboard để tự kéo số liệu, tự chạy prompt, tự gửi email. Cần code — làm ở bước sau khi đã quen với output của agent.

**Giới hạn cần biết:**

Agent không tự biết context lịch sử nếu không cung cấp. Mỗi tuần cần paste thêm số liệu tuần trước để so sánh chính xác.

# English

Input used to generate this output:

> I want to automate writing weekly campaign reports. Currently I spend 3-4 hours every Monday consolidating numbers from multiple sources, writing commentary, and sending to the team. I have data from an internal dashboard and don't know how to code.

**Best agent type: Analysis + Reporting Agent (no-code)**

This can be solved immediately with a prompt-based agent — no code needed. The flow: you copy numbers from the dashboard, paste into Claude with a prompt, the agent analyzes and writes the complete report.

**Start today:**

Create this prompt template and save it to reuse each week:

```
You are an analyst for a growth team. Here are the numbers for week [X]:
[Paste numbers]

Write a weekly report with:
- 3 key highlights (positive or negative)
- Comparison to last week
- 2-3 specific action recommendations for next week
- Concise format, readable in 2 minutes
```

Estimated time saved: from 3-4 hours down to 30-45 minutes.

**To fully automate, you'd also need:**

A Python script connecting to your dashboard API to pull numbers automatically, run the prompt, and send the email. Requires code — do this later once you're comfortable with the agent's output.

**Key limitation:**

The agent doesn't know historical context unless you provide it. Each week you'll still need to paste the previous week's numbers for accurate comparisons.
