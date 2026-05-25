# Case Study 01 — Dormant User Reactivation

## Bối cảnh

Fintech app tại Đông Nam Á. Segment: user có balance trong ví nhưng không có giao dịch trong 30-60 ngày. Pool: khoảng 15% tổng user base.

Mục tiêu: reactivate 10% segment này trong 3 tuần.

## Prompt sử dụng

Campaign Brief Agent (xem 02-your-first-campaign-agent/prompt.md)

Input:
- Target segment: Dormant user 30-60 ngày, có balance > 10K
- Mục tiêu: 10% reactivation rate trong 21 ngày
- Budget: 50 triệu VND
- Mechanic: Cashback
- Timeline: 3 tuần

## Output agent trả về

Thời gian tạo brief: 6 phút.

Agent đề xuất mechanic cashback có trigger rõ ràng: user hoàn thành giao dịch đầu tiên sau 30 ngày không active thì nhận cashback ngay lập tức. Có checklist đầy đủ trước launch bao gồm segment export, tracking verification, và budget cap.

Phần flag rủi ro agent tự động thêm vào: cần theo dõi D7 retention sau reactivation để biết user có thực sự quay lại hay chỉ lấy cashback rồi biến.

## Kết quả thực tế (ẩn danh số liệu)

- Reactivation rate: vượt target, đạt trên 12%
- Cost per reactivated user: dưới mức budget kế hoạch
- D7 retention của reactivated user: thấp hơn expected, dẫn đến quyết định thêm touchpoint thứ hai

## Bài học

Agent tự động flag đúng vấn đề quan trọng nhất (D7 retention) trong phần rủi ro. Nếu chỉ đọc số tổng và báo cáo reactivation rate thì bỏ qua vấn đề này.

Prompt tiết kiệm khoảng 2.5 tiếng so với viết brief thủ công, nhưng giá trị lớn nhất không phải ở thời gian mà ở việc không bỏ sót rủi ro.

---

# English

## Context

Fintech app in Southeast Asia. Segment: users with wallet balance but no transactions in the past 30-60 days. Pool size: approximately 15% of total user base.

Goal: reactivate 10% of this segment within 3 weeks.

## Prompt used

Campaign Brief Agent (see 02-your-first-campaign-agent/prompt.md)

## Real results (anonymized)

Reactivation rate exceeded target at above 12%. Cost per reactivated user came in below budget. D7 retention of reactivated users was lower than expected, leading to a decision to add a second touchpoint.

## Key lesson

The agent automatically flagged the most important risk (D7 retention) in the risk section. Looking only at the reactivation rate headline would have missed this.

The prompt saved approximately 2.5 hours vs writing the brief manually. But the bigger value was not missing a critical risk.
