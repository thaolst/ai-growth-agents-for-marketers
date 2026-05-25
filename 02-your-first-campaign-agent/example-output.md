# Example output — Campaign Brief Agent

Input dùng để tạo output này (fictional):

> Target segment: User có ví nhưng không có giao dịch trong 30+ ngày. Mục tiêu: reactivate 15% dormant user trong 4 tuần. Budget: 50 triệu VND. Mechanic: Cashback. Timeline: 3 tuần.

**Tổng quan campaign**
- Tên: Wake Up Wednesday
- Mục tiêu: Reactivate dormant user có balance bằng cashback có trigger rõ ràng
- Metric thành công: 15% reactivation rate (dormant → 1 giao dịch trong thời gian campaign)

**Target segment**
- Ai: User có balance ví > 10K VND, không có giao dịch trong 30 ngày qua, đã đăng ký 60+ ngày
- Tại sao: Cuối tháng — user đang kiểm tra tài chính, intent giao dịch cao hơn
- Ước tính quy mô: dùng data thực tế từ dashboard để xác định pool

**Thiết kế mechanic**
- Loại: Cashback có trigger
- Hành trình user: Mở app → push cá nhân hóa → landing page → giao dịch ≥ 20K VND → nhận 10K cashback ngay
- Trigger: Giao dịch đầu tiên sau 30 ngày không active
- Phần thưởng: 10K VND cashback cho giao dịch ≥ 20K VND (tối đa 1 lần/user)

**Timeline**
- Pre-launch (ngày 1-3): Segment user, setup tracking, chuẩn bị push copy, QA mechanic
- Launch: Ngày 4 (thứ Tư)
- Checkpoint ngày 7: Review open rate và CTR
- Checkpoint ngày 14: Review conversion, quyết định gia hạn không
- Kết thúc: Ngày 21

**Phân bổ budget**
- Cashback reward: 45 triệu (ước tính 4,500 redemption × 10K)
- Buffer: 5 triệu
- Tổng: 50 triệu VND

**Metrics**
- KPI chính: Reactivation rate — target 15%
- KPI phụ: Cost per reactivated user (target < 12K VND), D7 retention (target > 40%)

**Rủi ro và xử lý**
- Push open rate thấp → A/B test 2 copy, gửi lúc 7 giờ tối
- User lấy reward rồi dormant lại → Track D7 retention, thêm touchpoint thứ hai
- Budget hết sớm → Cap 4,500 redemption, monitor hàng ngày

**Checklist trước launch**
- [ ] Segment đã export và verified
- [ ] Cashback mechanic đã config trên promotion platform
- [ ] Push notification copy đã được approve
- [ ] Tracking events đang fire đúng
- [ ] Budget cap đã set trong hệ thống
- [ ] Rollback plan đã document

# English

Input used to generate this output (fictional):

> Target segment: Users with wallet balance but no transaction in 30+ days. Goal: reactivate 15% of dormant users in 4 weeks. Budget: 50M VND. Mechanic: Cashback. Timeline: 3 weeks.

**Campaign overview**
- Name: Wake Up Wednesday
- Objective: Reactivate dormant users with balance via clearly triggered cashback
- Success metric: 15% reactivation rate (dormant → 1 transaction within campaign window)

**Target segment**
- Who: Users with wallet balance > 10K VND, zero transactions in last 30 days, registered 60+ days ago
- Why: End of month — users are checking finances, transaction intent is higher
- Estimated pool size: use actual dashboard data to determine

**Mechanic design**
- Type: Triggered cashback
- User journey: Opens app → personalized push → campaign landing page → transaction ≥ 20K VND → receives 10K cashback instantly
- Trigger: First transaction after 30-day dormancy
- Reward: 10K VND cashback on transaction ≥ 20K VND (max 1 per user)

**Timeline**
- Pre-launch (days 1-3): Segment users, setup tracking, prepare push copy, QA mechanic
- Launch: Day 4 (Wednesday)
- Day 7 checkpoint: Review open rate and CTR
- Day 14 checkpoint: Review conversion, decide whether to extend
- End: Day 21

**Budget breakdown**
- Cashback rewards: 45M (est. 4,500 redemptions × 10K)
- Buffer: 5M
- Total: 50M VND

**Metrics**
- Primary KPI: Reactivation rate — target 15%
- Secondary: Cost per reactivated user (target < 12K VND), D7 retention (target > 40%)

**Risks and mitigations**
- Low push open rate → A/B test 2 copy versions, send at 7PM
- Users claim reward then go dormant again → Track D7 retention, add second touchpoint
- Budget exhausted early → Cap at 4,500 redemptions, monitor daily

**Pre-launch checklist**
- [ ] Segment exported and verified
- [ ] Cashback mechanic configured in promotion platform
- [ ] Push notification copy approved
- [ ] Tracking events firing correctly
- [ ] Budget cap set in system
- [ ] Rollback plan documented
