# Example output — Agentic RAG

Query: "Campaign nào trước đây hiệu quả nhất với dormant user?"

Từ tài liệu trong project, mình tìm thấy 3 campaign nhắm vào dormant user:

Campaign tháng 3 (Brief_March_2024.pdf): Cashback 15% cho giao dịch đầu tiên sau 30 ngày không active. Kết quả: 11.2% reactivation rate, cost per reactivated user là 8,400 VND. Runtime 7 ngày.

Campaign tháng 7 (Q3_Report.pdf, trang 4): Personalized voucher dựa trên loại transaction trước đây của user. Kết quả: 14.8% reactivation rate, cost per reactivated user là 11,200 VND. Runtime 14 ngày.

Campaign tháng 11 (Campaign_Brief_Nov.docx): Flash sale 24h với flat discount 20%. Kết quả không được ghi rõ — chỉ có ghi nhận "performance below target", không có số cụ thể.

**Kết luận từ dữ liệu có sẵn:**

Campaign tháng 7 có reactivation rate cao nhất (14.8%) nhưng cost per user cũng cao hơn. Campaign tháng 3 hiệu quả về chi phí hơn nếu budget là constraint chính. Campaign tháng 11 thiếu data để đánh giá.

**Data gap:** Không có thông tin về D30 retention sau reactivation cho cả 3 campaign.

# English

Query: "Which past campaigns worked best for dormant users?"

From the documents in the project, I found 3 campaigns targeting dormant users:

March campaign (Brief_March_2024.pdf): 15% cashback on first transaction after 30 days of inactivity. Result: 11.2% reactivation rate, cost per reactivated user of 8,400 VND. Ran for 7 days.

July campaign (Q3_Report.pdf, page 4): Personalized voucher based on each user's past transaction type. Result: 14.8% reactivation rate, cost per reactivated user of 11,200 VND. Ran for 14 days.

November campaign (Campaign_Brief_Nov.docx): 24-hour flash sale with flat 20% discount. Results not clearly documented — only noted as "performance below target" with no specific numbers.

**Conclusion from available data:**

The July campaign had the highest reactivation rate (14.8%) but also higher cost per user. The March campaign was more cost-efficient if budget is the main constraint. The November campaign lacks data to evaluate.

**Data gap:** No information on D30 retention after reactivation for any of the 3 campaigns.
