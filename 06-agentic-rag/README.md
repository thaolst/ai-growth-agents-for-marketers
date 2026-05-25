# Agentic RAG

RAG là Retrieval-Augmented Generation — agent tìm thông tin liên quan từ một tập tài liệu lớn trước khi trả lời.

Ứng dụng thực tế trong growth marketing: thay vì mỗi lần cần thông tin phải tìm lại trong đống file cũ, bạn upload tất cả lên một lần, rồi hỏi agent như hỏi một người đã đọc hết tất cả.

Mình dùng cái này nhất để query lại campaign history — "campaign nào trước đây nhắm vào segment X có kết quả tốt?" hoặc "chúng ta đã thử mechanic Y chưa, kết quả thế nào?" Câu hỏi mất 30 phút tìm kiếm thủ công, với RAG mất 30 giây.

## Không cần setup phức tạp

Cách đơn giản nhất không cần code: upload tất cả file vào một Project trong Claude.ai, rồi hỏi thẳng trong project đó. Claude đọc được toàn bộ file trong project và trả lời dựa trên nội dung thật của chúng.

Cách có Python: xử lý được file lớn hơn và nhiều file hơn giới hạn của Claude.ai.

# English

RAG (Retrieval-Augmented Generation) means the agent finds relevant information from a large set of documents before answering.

In growth marketing: instead of searching through old files every time, upload everything once, then ask the agent like asking someone who has read all of it.

I use this most to query campaign history — "which past campaigns targeting segment X performed well?" That question takes 30 minutes manually, 30 seconds with RAG.

**No complex setup needed:** Upload all files into a Claude Project, ask questions directly in that project. Claude reads everything in the project and answers based on actual content.
