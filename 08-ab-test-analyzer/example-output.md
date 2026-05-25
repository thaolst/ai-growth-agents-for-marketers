# Example output — A/B Test Analyzer

Input (fictional): Test push notification copy. A: "Bạn có 50,000đ trong ví, dùng ngay hôm nay". B: "Hôm nay là ngày cuối để dùng ưu đãi của bạn". Chạy 14 ngày. Control: 45,000 user, 1,890 click (4.2%). Variant: 44,800 user, 2,464 click (5.5%).

**Winner: Variant B (urgency copy)**

B có conversion rate cao hơn A 30.9% (5.5% vs 4.2%). Với sample size ~45,000 mỗi nhóm và chênh lệch này, statistical significance trên 99% — khả năng đây chỉ là ngẫu nhiên dưới 1%.

Kết quả đáng tin, có thể ra quyết định ngay.

**Độ tin cậy**

Rất cao. Sample size đủ lớn, test chạy đủ dài (14 ngày bao phủ weekly behavior pattern), chênh lệch đủ lớn để không bị noise. Không cần chạy thêm.

**Insight từ segment breakdown**

Urgency copy hiệu quả hơn với cả hai segment nhưng tác động lớn hơn với new user (tăng 54.8%) so với existing user (tăng 17.3%).

New user phản ứng mạnh hơn với urgency — có thể vì chưa có habit dùng app, cần trigger mạnh hơn để hành động.

**Đề xuất**

Rollout variant B cho toàn bộ user. Nếu muốn tối ưu thêm, test tiếp với new user riêng — thử urgency mạnh hơn (deadline cụ thể, countdown) vì nhóm này phản ứng tốt nhất.

Lưu ý: theo dõi unsubscribe rate sau khi rollout — urgency copy đôi khi tăng short-term conversion nhưng tăng opt-out nếu dùng quá nhiều.

# English

Input (fictional): Push notification copy test. A: "You have 50,000đ in your wallet, use it today". B: "Today is the last day to use your offer". Ran 14 days. Control: 45,000 users, 1,890 clicks (4.2%). Variant: 44,800 users, 2,464 clicks (5.5%).

**Winner: Variant B (urgency copy)**

B outperformed A by 30.9% (5.5% vs 4.2%). With ~45,000 users per group and this size of difference, statistical significance is above 99% — less than 1% chance this is random.

Result is reliable. Safe to make a decision based on it.

**Confidence**

Very high. Sample size is sufficient, test ran long enough (14 days covers weekly behavior patterns), and the difference is large enough to not be noise. No need to run longer.

**Segment insight**

Urgency copy performed better across both segments but had stronger impact on new users (+54.8%) vs existing users (+17.3%).

New users respond more strongly to urgency — likely because they haven't built an app habit yet and need a stronger trigger to act.

**Recommendation**

Roll out variant B to all users. If you want to optimize further, run a follow-up test for new users specifically — try stronger urgency (specific deadline, countdown timer) since this group responds best to it.

Note: monitor unsubscribe rate after rollout — urgency copy can increase short-term conversion but also increase opt-outs if overused.
