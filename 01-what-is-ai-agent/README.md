# AI Agent là gì — góc nhìn của một growth marketer

Trước khi dùng AI agent, mình nghĩ nó là thứ gì đó phức tạp, cần biết code, cần setup nhiều thứ. Sau một thời gian dùng thực tế, mình hiểu ra điều đơn giản hơn nhiều.

Agent không phải chatbot trả lời câu hỏi. Agent là thứ **nhận một mục tiêu, tự quyết định các bước thực hiện, và trả về kết quả hoàn chỉnh** — không cần can thiệp từng bước.

Ví dụ thực tế trong growth marketing:

Chatbot: "Viết brief cho campaign voucher tháng 12"
Trả về một đoạn text, bạn phải tự format, tự điền thêm, tự kiểm tra.

Agent: "Mình có target MEU tháng 12 là X, budget Y, segment Z"
Tự phân tích segment, tự đề xuất mechanic, tự viết brief hoàn chỉnh, tự flag rủi ro.

Sự khác biệt không phải ở công nghệ. Mà ở cách bạn giao việc.

## Cách mình nghĩ về agent trong growth marketing

Mỗi agent giải quyết một loại công việc cụ thể. Mình không build agent "làm tất cả mọi thứ" — mình build nhiều agent nhỏ, mỗi cái làm một việc thật tốt.

| Loại công việc | Agent làm gì |
|----------------|-------------|
| Lên brief | Nhận 5 input, trả về brief hoàn chỉnh |
| Phân tích data | Nhận raw numbers, trả về insight và đề xuất |
| Lên plan | Nhận target, trả về roadmap chi tiết |
| Review campaign | Nhận kết quả cũ, trả về bài học và next steps |

## Tại sao không cần biết code để bắt đầu

Agent đơn giản nhất chỉ là một prompt được viết đủ tốt. Claude đọc prompt đó, hiểu vai trò của mình, hiểu task, và thực thi như một agent thật sự.

Code chỉ cần khi muốn agent tự chạy mà không cần trigger — ví dụ tự kéo data lúc 7 giờ sáng, tự gửi báo cáo, tự monitor campaign. Những thứ đó ở các phần sau.

Bắt đầu từ prompt. Từ từ thêm code khi cần.

# English

Before using AI agents, I thought they were complex, required coding, required lots of setup. After using them in real work, I understood something much simpler.

An agent is not a chatbot that answers questions. An agent **receives a goal, decides its own steps, and returns a complete result** — without you intervening at each step.

Real example in growth marketing:

Chatbot: "Write a brief for the December voucher campaign"
Returns a text block. You still format it, fill in gaps, check it yourself.

Agent: "I have a December MEU target of X, budget Y, segment Z"
Analyzes the segment, suggests the mechanic, writes the complete brief, flags risks — on its own.

The difference is not the technology. It's how you delegate.

## How I think about agents in growth marketing

Each agent solves one specific type of work. I don't build agents that "do everything" — I build multiple small agents, each doing one thing well.

| Type of work | What the agent does |
|--------------|---------------------|
| Write brief | Takes 5 inputs, returns complete brief |
| Analyze data | Takes raw numbers, returns insights and recommendations |
| Build plan | Takes target, returns detailed roadmap |
| Review campaign | Takes past results, returns lessons and next steps |

## Why you don't need code to start

The simplest agent is just a well-written prompt. Claude reads it, understands its role, understands the task, and executes like a real agent.

Code is only needed when you want the agent to run without you triggering it — pulling data at 7am, sending reports automatically, monitoring campaigns. That comes in later sections.

Start with prompts. Add code gradually when needed.
