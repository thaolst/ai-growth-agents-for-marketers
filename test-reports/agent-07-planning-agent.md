# Test Report: Agent 07 — Planning Agent
> Tested: 2026-05-28 21:42 GMT+7

## Scenario
Monthly plan — June 2026, tăng MEU từ 2M → 2.5M (+25%).

## Input
```json
{
  "period": "June 2026",
  "metric": "MEU (Monthly Engaging Users)",
  "target": "2,500,000",
  "baseline": "2,000,000",
  "budget": "5 tỷ VND",
  "team": "5 people (1 SM, 2 campaign, 1 data, 1 creative)",
  "channels": "push, in-app, email, Zalo OA",
  "context": "Tháng thường — không có dịp đặc biệt. Competitor đang chạy cashback 20%",
  "lessons": "Tháng 5: game mechanic có click rate cao nhưng conversion thấp. Voucher trực tiếp vẫn hiệu quả nhất với new user",
  "constraints": "Không giảm quá 30% giá trị voucher. Segment VIP không nhận campaign mass",
  "deadline": "Campaign thứ 2 phải live trước 10/06"
}
```

## Output

### 1. Phân tích tình huống
- **Gap**: +500k MEU (+25%) — tham vọng cho tháng thường
- **Challenge**: Không có dịp đặc biệt để dựa vào, competitor đang aggressive với cashback
- **Lesson**: Game không convert = cần ưu tiên mechanic trực tiếp (voucher)
- **Cơ hội**: Có data từ tháng 5 → targeting chính xác hơn

### 2. Strategy
**"Direct + Retain"**: 
- Đầu tháng: Voucher trực tiếp cho user đang inactive (dễ convert nhất)
- Giữa tháng: Mechanic kết hợp (voucher + game nhẹ) cho user đang active
- Cuối tháng: Retarget cho user đã convert nhưng chưa quay lại

### 3. Campaign Breakdown
| # | Campaign | Target | Budget | Priority |
|---|----------|--------|--------|----------|
| 1 | Re-engagement: Inactive 14d + voucher 30k | 800k users | 1.5B | 🔴 P0 |
| 2 | Mid-month booster: Mua 1 tặng 1 + mini game | 1.2M users | 2B | 🔴 P0 |
| 3 | Weekend flash: Cashback 15% (Th7-CN) | 1.5M users | 1B | 🟡 P1 |
| 4 | End-month retarget: Push reminder cho user còn 7d | 500k users | 0.5B | 🟢 P2 |

### 4. Budget Allocation
| Campaign | Budget | % | Rationale |
|----------|--------|---|-----------|
| #1 Re-engagement | 1.5B | 30% | Highest conversion potential (15-20% expected) |
| #2 Mid-month | 2B | 40% | Volume driver |
| #3 Weekend flash | 1B | 20% | Low cost, incremental |
| #4 Retarget | 0.5B | 10% | Safety net — catch remaining gap |

### 5. Timeline
```
W1 (1-7/6): Campaign #1 live → re-engage inactive
W2 (8-14/6): #1 continues + #2 setup → #2 live before 10/06
W3 (15-21/6): #2 peak + #3 weekend (Sat-Sun)
W4 (22-28/6): #2 wrap + #4 starts
Review: Daily check MEU pacing vs target
```

### 6. Risks
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Re-engagement ROI thấp hơn expected | Medium | Chuyển budget sang campaign #2 sớm |
| Competitor tăng cashback | High | Có sẵn contingency cho emergency voucher |
| Campaign #2 không live kịp 10/06 | High | Parallel execution từ W1 — không chờ #1 kết thúc |
| MEU gap cuối tháng vẫn còn | Medium | Activate end-month retarget sớm hơn dự kiến |

## Đánh giá

| Tiêu chí | Điểm | Nhận xét |
|----------|------|----------|
| **Structure** | 9/10 | Có framework rõ ràng, dễ follow |
| **Actionable** | 8/10 | Campaign breakdown cụ thể, có timeline |
| **Budget logic** | 8/10 | Allocation có rationale, tỷ lệ hợp lý |
| **Risk aware** | 7/10 | Có mitigations nhưng thiếu contingency plan định lượng |
| **Lessons applied** | 8/10 | Game không hiệu quả → ưu tiên voucher, đúng |
| **Overall** | **8.0/10** | Plan dùng được, cần workshop với team để refine số |
