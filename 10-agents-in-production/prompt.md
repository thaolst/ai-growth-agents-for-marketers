# Prompt — Review agent trước khi deploy

Dùng khi: bạn đã build một agent và muốn kiểm tra kỹ trước khi dùng thật.

Paste vào Claude:
Mình có agent sau đây và muốn review trước khi dùng thật trong công việc.

**Mô tả agent:**
[Agent này làm gì, nhận input gì, trả về output gì]

**System prompt / prompt template đang dùng:**
[Paste prompt vào đây]

**Ví dụ input thật:**
[Paste một ví dụ input thật]

**Output agent trả về với input trên:**
[Paste output]

Hãy review và cho mình biết:

1. Điểm yếu của prompt — chỗ nào có thể khiến agent cho kết quả sai hoặc không nhất quán
2. Edge cases mình chưa nghĩ đến — những tình huống input bất thường có thể làm agent fail
3. Cách cải thiện prompt để output ổn định hơn
4. Những gì mình nên monitor khi agent chạy thật — dấu hiệu nào cho thấy agent đang sai
5. Với use case này, mình có nên deploy hay cần thêm testing không

*English version*

I have the following agent and want to review it before using it in real work.

**Agent description:**
[What it does, what input it takes, what output it returns]

**System prompt / prompt template being used:**
[Paste here]

**Example real input:**
[Paste one real example]

**Output the agent returned:**
[Paste output]

Review and tell me:
1. Prompt weaknesses — where could it produce inconsistent or wrong results
2. Edge cases not handled — unusual inputs that could cause failures
3. How to improve the prompt for more stable output
4. What to monitor when running in production — warning signs
5. Should I deploy now, keep testing, or redesign
