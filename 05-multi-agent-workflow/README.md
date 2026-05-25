# Multi-Agent Workflow

Một agent làm một việc tốt. Nhiều agent phối hợp làm được cả một workflow.

Ví dụ thực tế: mình muốn lên campaign plan dựa trên phân tích campaign cũ. Trước đây có hai bước tách biệt — đọc lại campaign cũ rồi viết plan mới. Với multi-agent, mình setup một pipeline: Agent 1 đọc và phân tích data campaign cũ, Agent 2 nhận output của Agent 1 và dùng nó để viết plan mới. Mình chỉ cần đưa input đầu tiên, nhận output cuối cùng.

## Khi nào cần multi-agent

Khi công việc có nhiều bước mà output của bước này là input của bước kia. Khi một bước đòi hỏi "vai" khác với bước còn lại — ví dụ analyst và strategist cần nhìn vào cùng một vấn đề theo hai góc khác nhau.

## Khi một agent vẫn đủ

Nếu công việc chỉ có một bước, hoặc bạn có thể làm tất cả trong một prompt, không cần multi-agent. Đừng over-engineer.


# English

One agent does one thing well. Multiple agents working together can handle an entire workflow.

Real example: I want to build a campaign plan based on analysis of past campaigns. Previously that was two separate steps — read old campaigns, then write the new plan. With multi-agent, I set up a pipeline: Agent 1 reads and analyzes past campaign data, Agent 2 takes Agent 1's output and uses it to write the new plan. I give the first input and receive the final output.

## When you need multi-agent

When work has multiple steps where the output of one step is the input of the next. When different steps require different "roles" — for example, an analyst and a strategist need to look at the same problem from different angles.

## When one agent is enough

If the work is one step, or you can do everything in a single prompt, multi-agent isn't needed. Don't over-engineer.
