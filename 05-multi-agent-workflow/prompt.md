# Prompt — Multi-agent: Research + Plan

Đây là cách chạy hai agent nối tiếp nhau mà không cần code.

**Bước 1 — Research Agent**

Mở cuộc trò chuyện mới trong Claude, paste prompt này:

Bạn là analyst. Nhiệm vụ của bạn là đọc dữ liệu campaign sau và rút ra insight để một strategist có thể dùng ngay.

[Paste data campaign hoặc đính kèm file]

Trả về dưới dạng JSON với các field:
- top_performing_mechanics: list mechanic có kết quả tốt nhất và tại sao
- underperforming_areas: list những gì không work và lý do nghi ngờ
- segment_insights: nhóm user nào phản ứng tốt/kém
- recommended_focus: 3 điểm strategist nên ưu tiên cho campaign tiếp theo
- data_gaps: những gì còn thiếu để phân tích đầy đủ hơn

Chỉ trả về JSON, không giải thích thêm.

Copy toàn bộ JSON output.

**Bước 2 — Strategy Agent**

Mở cuộc trò chuyện mới, paste prompt này:

Bạn là growth strategist. Bạn nhận được analysis sau từ analyst:

[Paste JSON từ bước 1]

Dựa trên analysis này, viết campaign plan cho tháng tới:
- Target: [điền vào]
- Budget: [điền vào]
- Timeline: [điền vào]

Lên plan cụ thể, giải thích tại sao mỗi quyết định dựa trên insight từ analysis.

# English

This is how to run two agents in sequence without code — just two separate conversations in Claude.

**Step 1 — Research Agent**

Open a new conversation in Claude, paste this prompt:

You are an analyst. Your job is to read the following campaign data and extract insights that a strategist can use immediately.

[Paste campaign data or attach files]

Return as JSON with these fields:
- top_performing_mechanics: list mechanics that performed best and why
- underperforming_areas: list what didn't work and suspected reasons
- segment_insights: which user groups responded well or poorly
- recommended_focus: top 3 things a strategist should prioritize next
- data_gaps: what information is missing for more complete analysis

Return only JSON, no additional explanation.

Copy the full JSON output.

**Step 2 — Strategy Agent**

Open a new conversation, paste this prompt:

You are a growth strategist. You received the following analysis from your analyst:

[Paste JSON from Step 1]

Based on this analysis, write a campaign plan for next month:
- Target: [fill in]
- Budget: [fill in]
- Timeline: [fill in]

Make the plan specific. Justify each decision using insights from the analysis.
