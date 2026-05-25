# Prompt — A/B Test Analyzer

Dùng khi: bạn có kết quả A/B test và muốn biết winner, độ tin cậy, và nên làm gì tiếp.

Copy toàn bộ phần dưới, paste vào Claude, điền số liệu thật của bạn:
Bạn là data analyst chuyên về growth marketing experiment. Phân tích A/B test sau và trả lời bằng ngôn ngữ mà một marketer không có background thống kê có thể hiểu và ra quyết định ngay.

**Thông tin test:**
- Tên test: [mô tả ngắn]
- Hypothesis: [bạn muốn kiểm chứng điều gì]
- Ngày bắt đầu: [ngày]
- Ngày kết thúc / số ngày đã chạy: [số ngày]
- Primary metric: [conversion rate / click rate / transaction rate / v.v.]

**Kết quả:**

Control (A):
- Số user: [số]
- Số conversion: [số]
- Conversion rate: [%]

Variant (B):
- Số user: [số]
- Số conversion: [số]
- Conversion rate: [%]

**Secondary metrics (nếu có):**
- [metric 2]: Control [số] vs Variant [số]
- [metric 3]: Control [số] vs Variant [số]

**Segment breakdown (nếu có):**
- [ví dụ: new user — Control X% vs Variant Y%]
- [existing user — Control X% vs Variant Y%]
Từ data trên, cho mình biết:

1. Winner là A hay B, hay chưa có winner — giải thích ngắn gọn tại sao
2. Độ tin cậy của kết quả này — có nên ra quyết định dựa vào nó không
3. Nếu chưa đủ tin cậy — cần thêm bao nhiêu sample hoặc bao nhiêu ngày
4. Insight đáng chú ý từ segment breakdown nếu có
5. Đề xuất hành động cụ thể: rollout, tiếp tục test, hay dừng

# English

Use when: you have A/B test results and want to know the winner, confidence level, and what to do next.

Copy everything below, paste into Claude, fill in your actual numbers:

You are a data analyst specializing in growth marketing experiments. Analyze this A/B test and respond in plain language that a marketer without a statistics background can understand and act on immediately.

**Test info:**
- Test name: [short description]
- Hypothesis: [what were you testing]
- Start date: [date]
- End date / days run: [number of days]
- Primary metric: [conversion rate / click rate / transaction rate / etc.]

**Results:**

Control (A):
- Users: [number]
- Conversions: [number]
- Conversion rate: [%]

Variant (B):
- Users: [number]
- Conversions: [number]
- Conversion rate: [%]

**Secondary metrics (if any):**
- [metric 2]: Control [number] vs Variant [number]

**Segment breakdown (if any):**
- [e.g. new users — Control X% vs Variant Y%]

Tell me: winner (A, B, or none yet) and why, confidence level and whether to act on this, how much more sample or time if not confident yet, any notable segment patterns, and recommended action: rollout, keep testing, or stop.
