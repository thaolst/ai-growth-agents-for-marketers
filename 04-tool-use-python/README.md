# Tool Use — Python

Phần trước (03) là agent đọc những gì bạn paste vào. Phần này là agent **tự đi lấy data** mà không cần bạn copy-paste thủ công.

Sự khác biệt thực tế: thay vì mỗi sáng thứ Hai bạn mở dashboard, copy số liệu, paste vào Claude — bạn chạy một script, nó tự kéo data, tự phân tích, tự xuất report.

Mình bắt đầu dùng phần này sau khoảng 2 tuần dùng prompt thuần. Khi đã biết mình muốn agent làm gì, thêm Python vào chỉ là để bỏ đi bước thủ công.

## Những gì agent Python có thể làm mà prompt thuần không làm được

Tự kéo data từ Google Sheets hoặc file CSV theo lịch định sẵn. Tự gửi kết quả qua email hoặc Slack khi xong. Chạy lúc nửa đêm để sáng có sẵn report. Xử lý file lớn mà paste vào Claude không được vì quá dài.

## Không cần biết code để bắt đầu

Script trong folder này được viết để chạy được ngay mà không cần hiểu từng dòng. Bạn chỉ cần biết cách mở Terminal, chạy lệnh, và điền đúng file path.

Nếu có lỗi — copy lỗi đó paste vào Claude, hỏi "lỗi này nghĩa là gì và fix thế nào". Đó là cách mình học.


# English

The previous section (03) was an agent that reads what you paste into it. This section is an agent that **goes and gets the data itself** without you copy-pasting manually.

The practical difference: instead of opening a dashboard every Monday, copying numbers, and pasting into Claude — you run a script, it pulls the data, analyzes it, and outputs the report.

I started using this part after about 2 weeks of using prompts alone. Once I knew what I wanted the agent to do, adding Python was just about removing the manual step.

## What Python agents can do that prompts alone cannot

Pull data from Google Sheets or CSV files on a schedule. Send results via email or Slack automatically. Run at midnight so reports are ready in the morning. Process files too large to paste into Claude.

## You don't need to know code to get started

The scripts here are written to run immediately without understanding every line. You just need to know how to open Terminal, run a command, and edit a file path.

If something breaks — copy the error into Claude and ask "what does this error mean and how do I fix it." That's how I learned.
