# Example output — Multi-agent workflow

Ví dụ pipeline: phân tích Q2 → lên plan Q3.

**Output Agent 1 (Research):**

```json
{
  "top_performing_mechanics": [
    {"mechanic": "cashback_tiered", "why": "Higher tier reward drove 2.3x more repeat transactions vs flat cashback"},
    {"mechanic": "streak_bonus", "why": "7-day streak users had 4x higher D30 retention"}
  ],
  "underperforming_areas": [
    {"area": "new_user_vouchers", "suspected_reason": "Voucher value too low relative to minimum transaction requirement"},
    {"area": "flash_sales", "suspected_reason": "Training users to wait for discounts, hurting organic baseline"}
  ],
  "segment_insights": {
    "high_response": "Users aged 25-34, urban, transaction frequency 3-5x/month",
    "low_response": "Users with only 1 transaction in last 60 days — needs higher trigger incentive"
  },
  "recommended_focus": [
    "Double down on streak mechanics for retention",
    "Redesign new user onboarding incentive — increase value or lower barrier",
    "Phase out flash sales, replace with personalized offers"
  ],
  "data_gaps": ["No data on what users do after voucher expires", "No segment data by geography"]
}
```

**Output Agent 2 (Strategy) — dùng JSON trên làm input:**

Q3 plan tập trung vào hai thứ: giữ user đang có tốt hơn và cải thiện new user conversion.

Streak program mở rộng — tiếp tục mechanic đang work, tăng reward ở milestone 14 ngày và 30 ngày để giữ user lâu hơn. Budget: 40% tổng.

New user redesign — tăng voucher value 50% nhưng giảm minimum transaction requirement. Test với cohort nhỏ trước. Budget: 25%.

Personalized offer pilot — thay thế dần flash sale bằng offer dựa trên transaction history của từng user. Bắt đầu với top 20% user theo value. Budget: 25%.

Buffer: 10% — giữ lại để react với kết quả tháng 7.


# English

Example pipeline: analyze Q2 → build Q3 plan.

Agent 1 output (Research): JSON with top performing mechanics (cashback tiered drove 2.3x more repeat transactions; streak bonus gave 4x higher D30 retention), underperforming areas (new user vouchers had low uptake; flash sales trained users to wait), segment insights (best response from 25-34 urban users with 3-5 transactions/month), and recommended focus (double down on streak mechanics, redesign new user incentive, phase out flash sales).

Agent 2 output (Strategy): Q3 plan focuses on two things — retaining existing users better and improving new user conversion. Streak program expanded with higher rewards at 14-day and 30-day milestones (40% of budget). New user redesign with 50% higher voucher value but lower minimum transaction (25%). Personalized offer pilot replacing flash sales starting with top 20% users by value (25%). Buffer 10%.
