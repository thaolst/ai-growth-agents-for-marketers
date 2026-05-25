# Agents in Production

Chạy agent trong Claude.ai là một chuyện. Chạy agent tự động, không cần bạn trigger, chạy đúng giờ mỗi ngày — là chuyện khác.

Phần này là những gì mình học được khi đưa agent từ "thử nghiệm trên máy" thành "chạy thật trong workflow hàng ngày". Không phải kỹ thuật — mà là những quyết định và bài học thực tế.

## Trước khi deploy bất kỳ agent nào

Chạy thủ công ít nhất 10-20 lần với data thật. Không phải để test code — mà để hiểu agent fail ở đâu, output có đủ tin cậy không, và bạn cảm thấy yên tâm dùng kết quả của nó để ra quyết định chưa.

Mình không deploy agent nào mà mình chưa dùng thủ công đủ lâu để biết nó hay sai ở đâu.

## Những gì hay sai trong production

Agent trả về format khác đột nhiên — code của bạn parse sai, không có gì break rõ ràng nhưng kết quả im lặng sai. Fix: luôn validate output trước khi dùng, không assume format luôn nhất quán.

Data đầu vào thay đổi — cột trong CSV được đổi tên, API trả về field mới. Agent không báo lỗi nhưng bỏ qua data quan trọng. Fix: log input và output của mỗi lần chạy, review hàng tuần.

Agent tự tin quá mức với data thiếu — khi input ít hơn bình thường, agent vẫn trả về kết quả trông có vẻ ổn. Fix: thêm check "nếu data dưới ngưỡng X thì flag thay vì tự phân tích".

## Nguyên tắc mình giữ

Agent hỗ trợ quyết định, không thay thế quyết định. Mình review output của agent trước khi dùng cho bất kỳ thứ gì ảnh hưởng đến user thật. Cái này không thay đổi dù agent đã chạy ổn định bao lâu.


# English

Running an agent in Claude.ai is one thing. Running an agent automatically, without you triggering it, at the right time every day — is another.

This section covers what I learned moving agents from "experimenting on my laptop" to "actually running in my daily workflow." Not technical details — the decisions and lessons learned in practice.

## Before deploying any agent

Run it manually at least 10-20 times with real data. Not to test the code — but to understand where the agent fails, whether the output is reliable enough to make decisions from, and whether you're comfortable trusting its results.

I don't deploy any agent I haven't used manually long enough to know where it tends to go wrong.

## What commonly breaks in production

Agent returns a different format unexpectedly — your code parses it wrong, nothing obviously breaks but results are silently wrong. Fix: always validate output before using it.

Input data changes — a column in your CSV gets renamed, an API returns a new field. Agent doesn't error but silently skips important data. Fix: log input and output from every run, review weekly.

Agent is overconfident with sparse data — when input is less than usual, the agent still returns results that look fine. Fix: add a check: if data is below threshold X, flag it instead of auto-analyzing.

## Principles I keep

Agents support decisions, they don't replace them. I review agent output before using it for anything that affects real users. This doesn't change no matter how long the agent has been running smoothly.
