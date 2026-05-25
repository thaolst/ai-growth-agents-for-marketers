# Example output — Agent review trước deploy

Input: review Campaign Brief Agent trước khi dùng thật.

**Điểm yếu của prompt hiện tại**

Prompt không có instruction xử lý khi input thiếu field quan trọng. Nếu không điền budget hoặc timeline, agent vẫn viết brief như thể có đủ thông tin — brief trông đầy đủ nhưng assumption sai. Thêm instruction: "nếu thiếu field quan trọng, hỏi lại thay vì tự đặt assumption."

Không có giới hạn về độ cụ thể của target segment. Input quá rộng như "tất cả user" sẽ cho brief chung chung.

**Edge cases chưa xử lý**

Budget rất nhỏ so với target — agent vẫn viết brief bình thường mà không flag target không thực tế.
Mechanic không phù hợp với segment — agent không có context để biết đây là bất thường.
Timeline quá ngắn — agent không biết internally bao lâu là đủ để prep.

**Cải thiện đề xuất**

Thêm bước sanity check cuối brief: "Với budget X và timeline Y, mục tiêu Z có khả thi không? Nếu không, flag rõ."

**Nên deploy không?**

Deploy được cho draft brief nội bộ. Chưa nên dùng output trực tiếp làm brief chính thức gửi stakeholder — vẫn cần review theo context nội bộ mà agent không biết.

# English

Input: review Campaign Brief Agent before using it in real work.

**Prompt weaknesses**

No instruction for handling missing important fields. If budget or timeline is left blank, the agent still writes a complete-looking brief based on wrong assumptions. Add: "if a critical field is missing, ask for it rather than assuming."

No constraint on how specific the target segment must be. Input as broad as "all users" will produce generic briefs.

**Unhandled edge cases**

Very small budget relative to target — agent writes a normal brief without flagging that the target is unrealistic.
Mechanic mismatched with segment — agent has no context to recognize this as unusual.
Timeline too short — agent doesn't know internally how long proper prep takes.

**Suggested improvement**

Add a sanity check at the end of the brief: "Given budget X and timeline Y, is goal Z achievable? If not, flag clearly."

**Should you deploy?**

Safe to deploy for internal draft briefs. Not yet ready to use output directly as official briefs sent to stakeholders — still needs review based on internal context the agent doesn't have access to.
