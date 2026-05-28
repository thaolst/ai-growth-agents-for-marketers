# Test Report: Agent 02 — Campaign Brief
> Tested: 2026-05-28 21:37 GMT+7

## Scenario
- **Target segment**: New users (0-7 days), urban Vietnam, 18-30
- **Mục tiêu**: Tăng first transaction rate từ 40% → 55%
- **Budget**: 500 triệu VND
- **Mechanic**: Voucher welcome + cashback
- **Timeline**: 4 tuần

## Input
```json
{
  "target_segment": "New users 0-7 days, urban Vietnam 18-30, đã download app nhưng chưa transaction",
  "campaign_objective": "Tăng first transaction rate từ 40% lên 55% trong 4 tuần",
  "budget": "500,000,000 VND",
  "mechanic_type": "voucher + cashback kết hợp",
  "timeline": "4 tuần (1-28 June 2026)"
}
```

## Output (AI-generated từ prompt)
I ran the Campaign Brief prompt with the inputs above. Here's the output:

### Campaign Overview
Tên campaign: **"First Step, Big Win"** — Welcome campaign cho new user chưa từng transaction.

Mục tiêu: Tăng first transaction rate từ 40% → 55% trên segment new user 0-7 ngày. Đây là mức tăng 37.5% so với baseline — tham vọng nhưng khả thi vì segment chưa từng được khuyến khích bằng voucher đúng cách.

### Target Segment
- **Nhân khẩu**: 18-30 tuổi, thành thị (HCMC, Hanoi, Đà Nẵng)
- **Hành vi**: Đã download app, đã explore features, nhưng chưa từng đặt transaction đầu tiên
- **Psychographic**: Có nhu cầu (đã tải app) nhưng cần push cụ thể để vượt rào cản trust + "ngại thử lần đầu"
- **Size ước tính**: ~50,000 users active trong 7 ngày qua chưa transact

### Mechanic Design
**Mechanic kép: welcome voucher + cashback milestone**

1. **Welcome voucher**: 50k VND giảm cho đơn đầu tiên, min spend 100k. (Kích thích hành động lần đầu — hạ barrier)
2. **Cashback 10%**: Hoàn 10% giá trị đơn đầu tiên, tối đa 50k, vào Ví Xu. (Tạo lý do quay lại — họ có Xu để dùng cho lần sau)
3. **Trigger**: Tự động kích hoạt khi user mở app lần 2-7 mà chưa transact — pop-up banner + push notification

**Lý do chọn**: New user cần 2 động lực:
- Lần 1: "Rẻ hơn bình thường" → voucher
- Lần 2+: "Có sẵn credit rồi, không dùng phí" → cashback vào Xu

### Timeline & Milestones
| Tuần | Hoạt động | Milestone |
|------|-----------|-----------|
| W1 | Setup + user targeting | Segment ready, push automation active |
| W2-3 | Launch + monitor | Target 45% first transaction rate |
| W4 | Optimization + wrap | Target 55%, A/B test voucher amount |

### Budget Breakdown
| Item | Amount |
|------|--------|
| Voucher (50k x 5,000 users) | 250,000,000 |
| Cashback (10% x 1,000 users x ~500k) | 50,000,000 |
| Push notification + comms | 30,000,000 |
| Contingency | 70,000,000 |
| **Total** | **400,000,000** |

### Metrics
- Primary: First transaction rate (target: +15pp → 55%)
- Secondary: D1 retention, D7 retention, voucher redemption rate
- Counter-metric: Cannibalization (users who would transact anyway without voucher)

### Risks
- **R1**: New user chỉ dùng voucher rồi bỏ — cashback vào Xu giúp giữ chân nhưng cần monitor
- **R2**: Budget cháy nếu conversion rate vượt target quá xa — set daily cap
- **R3**: Fraud (multiple accounts claim voucher) — cần device fingerprint từ đầu

### Checklist
- [ ] Segment validated với data team
- [ ] Push notification copy + timing ready
- [ ] Voucher code system tested
- [ ] Daily budget cap configured
- [ ] Xu system integration verified
- [ ] Fraud detection active

## Đánh giá

| Tiêu chí | Điểm (1-10) | Nhận xét |
|----------|-------------|----------|
| **Cụ thể, actionable** | 8/10 | Brief detail đủ để execute, có numbers rõ ràng |
| **SEA context** | 7/10 | Có đề cập Xu (phù hợp SEA fintech), nhưng thiếu insight về hành vi user VN cụ thể |
| **Budget realistic** | 8/10 | Phân bổ hợp lý, có contingency |
| **Risk aware** | 7/10 | Có fraud + cannibalization nhưng thiếu competitor reaction risk |
| **Overall** | **7.5/10** | Dùng được cho brief nhanh, cần edit thêm cho production |

## So với brief Thảo tự viết
Brief AI ra khung tốt, số liệu cụ thể, nhưng thiếu:
- Insight từ campaign history (cái gì từng fail)
- Context chính sách MoMo (Xu policy, budget threshold)
- Competitor landscape
