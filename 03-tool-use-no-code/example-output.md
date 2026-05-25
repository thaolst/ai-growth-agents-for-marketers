# Example output — Agent tổng hợp campaign

Input: 4 campaign brief từ Q1-Q2, chuẩn bị cho campaign Q3.
**Tóm tắt từng tài liệu:**

Campaign tháng 1 — Cashback 15% cho new user, target acquisition. CTR cao nhưng retention D7 thấp, phần lớn user không quay lại sau khi dùng hết cashback.

Campaign tháng 2 — Bundle voucher + game mechanic, target engagement. Engagement tốt hơn tháng 1 nhưng conversion thấp, user chơi game không chuyển sang transaction.

Campaign tháng 3 — Flash sale 24h, target transaction volume. Volume tăng đột biến ngày đầu, giảm nhanh. Margin bị ảnh hưởng do discount quá sâu.

Campaign tháng 4 — Loyalty tier reward, target retention. Retention cải thiện rõ rệt với user tier cao, không có tác động với new user và low-tier user.

**Pattern chung:**

Mechanic có thưởng ngay (cashback, flash sale) tạo spike ngắn hạn nhưng không giữ được user. Mechanic có yếu tố dài hạn (loyalty tier) hiệu quả hơn với user đã có habit nhưng không thu hút được user mới.

**Điểm bất thường:**

Tháng 2 có engagement cao nhưng conversion thấp — khoảng cách giữa "user thích chơi" và "user thực sự mua" lớn hơn dự kiến. Cần kiểm tra lại UX flow từ game sang transaction.

**3 insight cho Q3:**

Segment trước khi chọn mechanic — loyalty reward chỉ nên nhắm vào mid và high-tier user, acquisition mechanic cho new user. Dùng một mechanic cho tất cả đang làm loãng hiệu quả.

Flash sale tạo doanh thu ngắn hạn nhưng có thể đang train user chờ giảm giá thay vì mua bình thường. Cần tính cost dài hạn.

Game mechanic có potential nhưng cần có bridge rõ ràng từ game sang transaction — hiện tại đang bị đứt giữa chừng.

**Đề xuất cho campaign Q3:**

Tách riêng campaign cho new user (acquisition focus) và existing user (retention focus) thay vì chạy chung một mechanic. Với retention campaign, test thêm personalized reward dựa trên transaction history thay vì flat discount.

*English summary of output above*

Query: Synthesize 4 campaign briefs from Q1-Q2 to prepare for Q3.

Key patterns found: Mechanics with immediate rewards (cashback, flash sales) create short-term spikes but don't retain users. Long-term mechanics (loyalty tiers) work better for users who already have habits but don't attract new ones.

Notable: Month 2 had high engagement but low conversion — the gap between "users like playing" and "users actually transact" was larger than expected.

Top 3 insights for Q3: Segment before choosing mechanic. Flash sales may be training users to wait for discounts. Game mechanics need a clearer bridge to transaction.
