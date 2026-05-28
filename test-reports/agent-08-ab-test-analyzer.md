# Test Report: Agent 08 — A/B Test Analyzer
> Tested: 2026-05-28 21:40 GMT+7

## Scenario
A/B test cho campaign push notification — so sánh copy cũ (A) vs copy mới có personalization (B).

## Input
```json
{
  "test_name": "Push copy optimization — Welcome series",
  "hypothesis": "Personalized push (có tên user + offer cụ thể) sẽ tăng conversion rate so với copy generic",
  "start_date": "2026-05-20",
  "days_run": "8",
  "primary_metric": "Click-to-transaction rate"
}
```

**Results:**

Control (A) — Generic push:
- Users: 12,450
- Conversions: 498
- Rate: 4.0%

Variant (B) — Personalized:
- Users: 12,380
- Conversions: 581
- Rate: 4.69%

**Segment:**
- New user 0-7d: A: 3.2% vs B: 4.1%
- Existing user >30d: A: 4.5% vs B: 4.9%

## Output (AI-generated từ prompt)

### 1. Winner
**B — Personalized push là winner.** Conversion rate tăng từ 4.0% → 4.69%, tương đương +17.3% lift.

### 2. Độ tin cậy
Ở mức sample này (~12k user/nhánh), với conversion rate ~4%, kết quả có **statistical significance ở mức 95%+** (p-value ~0.02). Có thể ra quyết định dựa vào kết quả này.

### 3. Nếu cần thêm
Không cần — sample đã đủ lớn. Nếu rollout, nên monitor 1 tuần đầu để confirm kết quả replicate.

### 4. Segment insight
- **New user 0-7d** benefit nhiều nhất: +0.9pp (từ 3.2% → 4.1%), tương đương +28% lift
- **Existing user** gain ít hơn: +0.4pp
- **Gợi ý**: Personalization đặc biệt hiệu quả với new user — chưa có relationship với brand nên cần được "gọi tên" + offer rõ ràng

### 5. Đề xuất
**Rollout B cho tất cả user ngay.** Chi phí personalization gần như bằng 0 (chỉ thay đổi copy) nhưng lift +17%. 
Ưu tiên new user segment trước — đây là nhóm hưởng lợi nhiều nhất.

## Đánh giá

| Tiêu chí | Điểm | Nhận xét |
|----------|------|----------|
| **Kết luận rõ ràng** | 9/10 | Winner + giải thích dễ hiểu |
| **Statistical rigour** | 7/10 | Có nói significance nhưng không show p-value cụ thể hay confidence interval |
| **Segment insight** | 8/10 | Phát hiện new user benefit nhiều hơn — actionable |
| **Actionable recommendation** | 9/10 | Rollout — rõ ràng, không lằng nhằng |
| **Overall** | **8.3/10** | Output tốt, dùng được cho daily work |
