# Case Study 02 — A/B Test: Push Notification Copy

## Bối cảnh

Test 2 phiên bản push notification cho campaign engagement. Chạy 14 ngày, sample size lớn.

Mục tiêu: xác định copy nào drive higher transaction rate, và hiểu rõ hơn về hành vi theo từng segment.

## Prompt sử dụng

A/B Test Analyzer (xem 08-ab-test-analyzer/prompt.md)

## Vấn đề trước khi có prompt

Trước đây quy trình đọc kết quả A/B test mất khoảng 3 tiếng: đọc số từ tool, tính toán độ tin cậy, viết tóm tắt cho team, quyết định rollout hay không.

Hai lần trước đó, mình đã tuyên bố winner sai vì chỉ nhìn conversion rate tổng mà không kiểm tra sample size. Kết quả flip sau khi chạy thêm.

## Kết quả sau khi dùng prompt

Thời gian xử lý: 15 phút thay vì 3 tiếng.

Insight quan trọng nhất không phải từ overall result mà từ segment breakdown. Variant B win overall, nhưng win mạnh hơn rất nhiều với new user so với existing user. Điều đó dẫn đến quyết định khác với rollout cho tất cả: chỉ rollout cho new user trước, giữ lại existing user để test riêng.

## Bài học

Winner tổng có thể che giấu pattern quan trọng ở cấp segment. Prompt tự động phân tích breakdown này và đặt nó lên đầu thay vì để mình tự nhớ kiểm tra.

# English

## Context

A/B test of 2 push notification copy variants for an engagement campaign. Ran 14 days with large sample size.

Goal: identify which copy drives higher transaction rate, and understand behavior differences by segment.

## Problem before using the prompt

Previous process took about 3 hours: reading numbers from the analytics tool, calculating confidence levels, writing a summary for the team, deciding on rollout.

Twice before, a winner was declared incorrectly by looking only at overall conversion rate without checking sample size adequacy. Results flipped when the test continued.

## Results after using the prompt

Processing time: 15 minutes instead of 3 hours.

The most important insight came not from overall results but from segment breakdown. Variant B won overall but won significantly more with new users than existing users. This led to a different rollout decision: roll out to new users first, keep existing users for a separate test.

## Key lesson

Overall winners can mask important patterns at the segment level. The prompt automatically surfaces this breakdown instead of relying on the analyst to remember to check it.
