"""
Skill: Generate prompt + SKILL.md for a given topic + folder
"""
import os, json

TEMPLATES = {
    "campaign-monitor": {
        "title": "Campaign Monitor Agent",
        "desc_vi": "Agent theo dõi campaign real-time: KPI tracking, anomaly detection, auto-report.",
        "prompts_count": 4,
        "prompts": [
            {
                "name": "Campaign KPI Tracker",
                "use_case": "Khi cần theo dõi campaign đang chạy, check daily KPI vs target",
                "prompt": "Bạn là campaign monitor agent. Campaign [tên] đang chạy từ [ngày] đến [ngày]. Target: [KPI]. Daily actual: [số liệu]. Hãy:\n1. So sánh actual vs target\n2. Phát hiện anomaly (tăng/giảm đột biến)\n3. Đề xuất action nếu KPI dưới target",
                "output_example": "📊 Campaign T12 - Day 5\n• Actual: 45K / Target: 50K (90%)\n• So hôm qua: +12% ✅\n• Anomaly: Channel A giảm 30% do bid thấp\n• Action: Tăng bid Channel A lên 15%"
            },
            {
                "name": "Anomaly Detector",
                "use_case": "Khi có biến động KPI bất thường, cần phân tích nguyên nhân",
                "prompt": "Phát hiện anomaly: [KPI] thay đổi [X%] trong [khoảng thời gian]. Dữ liệu: [số liệu theo ngày]. Hãy:\n1. Xác định loại anomaly (seasonal / technical / external)\n2. Phân tích root cause\n3. Đề xuất response plan",
                "output_example": "🚨 Anomaly phát hiện: D7 retention giảm 25%\n• Loại: Technical (A/B test impact)\n• Root cause: New user flow thay đổi step 3\n• Response: Rollback trong 2h + notify team"
            }
        ]
    }
}

def run(topic, folder_name):
    if topic not in TEMPLATES:
        return {"error": f"Unknown topic: {topic}", "available": list(TEMPLATES.keys())}
    
    tpl = TEMPLATES[topic]
    
    # Tạo SKILL.md
    lines = [f"# {tpl['title']}", "", tpl["desc_vi"], ""]
    lines.append(f"## Prompts ({tpl['prompts_count']})")
    for p in tpl["prompts"]:
        lines.append(f"### {p['name']}")
        lines.append(f"**Khi nào dùng:** {p['use_case']}")
        lines.append("")
        lines.append("**Prompt:**")
        lines.append(f"```\n{p['prompt']}\n```")
        lines.append("**Ví dụ output:**")
        lines.append(f"```\n{p['output_example']}\n```")
        lines.append("")
    
    return {
        "folder": folder_name,
        "title": tpl["title"],
        "prompts": len(tpl["prompts"]),
        "skill_md": "\n".join(lines)
    }
