# MEU Planning Agent

MEU target là con số mình phải chịu trách nhiệm mỗi tháng. Áp lực là biết target nhưng không biết bắt đầu từ đâu — đặc biệt khi target tăng nhưng budget không tăng tương ứng.

Agent này làm ngược lại so với cách thông thường. Thay vì mình nghĩ campaign xong rồi mới tính xem đạt được bao nhiêu MEU — mình đưa target vào trước, agent tự tính ngược ra cần bao nhiêu campaign, cần mechanic gì, cần budget bao nhiêu.

Kết quả không phải lúc nào cũng tươi đẹp. Nhưng biết sớm còn hơn biết muộn.

## Input agent cần

- MEU target tháng này
- MEU hiện tại (baseline)
- Budget khả dụng
- Các channel đang có (push notification, in-app banner, email, v.v.)
- Constraint đặc biệt nếu có (không chạy discount sâu, không đụng segment X, v.v.)

## Output agent trả về

- Gap phân tích: cần thêm bao nhiêu MEU, từ đâu
- Breakdown theo segment: segment nào có potential cao nhất để đạt target
- Campaign plan gợi ý: mechanic, timeline, budget allocation
- Confidence level: khả năng thực tế đạt target với resource hiện có
- Plan B nếu plan chính không đủ

## Tại sao cái này tiết kiệm nhiều thời gian nhất

Trước đây mình mất 2-3 ngày để lên plan MEU — họp với team, align với nhiều bên, chỉnh đi chỉnh lại. Bây giờ mình dùng agent để có draft đầu tiên trong 30 phút, rồi mang draft đó vào họp để refine. Thời gian họp từ 2 tiếng xuống còn 45 phút vì mọi người đã có cái gì đó cụ thể để phản biện thay vì bắt đầu từ tờ giấy trắng.


# English

MEU target is the number I'm accountable for every month. The pressure is knowing the target but not knowing where to start — especially when targets increase but budget doesn't.

This agent works backward. Instead of thinking up a campaign and then calculating how much MEU it might produce — I give the target first, and the agent works backward to figure out what campaigns are needed, what mechanics, what budget.

The results aren't always pretty. But knowing early is better than knowing late.

## What the agent needs as input

- MEU target for this month
- Current MEU (baseline)
- Available budget
- Channels available (push notification, in-app banner, email, etc.)
- Any special constraints (no deep discounts, don't touch segment X, etc.)

## What the agent returns

Gap analysis, segment breakdown by potential, campaign plan with mechanics and budget, confidence level for hitting the target, and a Plan B if the primary plan isn't enough.

## Why this saves the most time

Previously I'd spend 2-3 days building a MEU plan — meetings, alignment, revisions. Now I use the agent to get a first draft in 30 minutes, then bring that draft into meetings to refine. Meeting time went from 2 hours to 45 minutes because everyone has something concrete to react to instead of starting from a blank page.
