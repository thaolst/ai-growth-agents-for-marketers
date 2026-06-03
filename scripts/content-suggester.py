#!/usr/bin/env python3
"""
Content Suggester — Script chạy 19:30 qua GitHub Actions
Quét repo, chọn topic theo lịch, gợi ý hook + angle, gửi Telegram.
"""
import json, os, sys
from datetime import datetime

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "1606915846")

# === AGENTS IN REPO ===
AGENTS = [
    {"folder": "01", "title": "AI Agent Consultant", "desc": "Tư vấn chọn agent phù hợp", "has_code": False},
    {"folder": "02", "title": "Campaign Brief Agent", "desc": "5 input sang brief hoàn chỉnh", "has_code": False},
    {"folder": "03", "title": "Campaign Synthesis", "desc": "Tổng hợp nhiều file campaign", "has_code": False},
    {"folder": "04", "title": "Automation Scripter", "desc": "Tự viết Python script", "has_code": True},
    {"folder": "05", "title": "Multi-Agent Pipeline", "desc": "Research ra Planning", "has_code": True},
    {"folder": "06", "title": "Agentic RAG", "desc": "Hỏi đáp từ campaign history", "has_code": False},
    {"folder": "07", "title": "Planning Agent", "desc": "Target sang campaign plan", "has_code": True},
    {"folder": "08", "title": "A/B Test Analyzer", "desc": "Phân tích và đề xuất", "has_code": True},
    {"folder": "09", "title": "MEU Planning Agent", "desc": "MEU target sang campaign plan", "has_code": True},
    {"folder": "10", "title": "Production Review", "desc": "Review agent trước deploy", "has_code": True},
]

# === WEEKLY SCHEDULE ===
PILLARS = {
    0: ("Growth Tip", "#growthtip"),
    1: ("Agent Demo", "#agentdemo"),
    2: ("Growth Tip", "#growthtip"),
    3: ("Agent Demo", "#agentdemo"),
    4: ("Growth Tip", "#growthtip"),
    5: ("Agent Demo", "#agentdemo"),
    6: ("Repo Update", "#repoupdate"),
}

WEEK_ROTATION = [
    ["02", "09"],  # Week 1: Campaign Brief + MEU
    ["08", "07"],  # Week 2: A/B Test + Planning
    ["06", "03"],  # Week 3: RAG + Synthesis
    ["04", "10"],  # Week 4: Scripter + Production
]

# === HOOK TEMPLATES ===
HOOKS = {
    "Agent Demo": [
        "Hôm nay mình dùng {agent}. Cách nó {desc}, khác hẳn làm tay.",
        "Mình vừa thử {agent} cho campaign tuần này. Output bất ngờ hơn tưởng tượng.",
        "Nếu bạn đang làm {desc}, agent này có thể giúp bạn tiết kiệm vài tiếng.",
    ],
    "Growth Tip": [
        "Phần mình thấy nhiều người hiểu sai nhất về {topic} là nghĩ nó phức tạp.",
        "Là Growth Marketing, {topic} không phải chuyện một sớm một chiều.",
        "Mẹo nhỏ: {topic}. Áp dụng AI agent vào việc này nhanh hơn bạn nghĩ.",
    ],
    "Case Study": [
        "Một campaign {topic} gần đây. Kết quả: {result}. Agent đã giúp gì?",
        "Case study tuần này: {topic}. Từ lúc có agent, thời gian phân tích giảm 80%.",
    ],
    "Repo Update": [
        "Tuần này repo có thêm gì mới: {update}. Cập nhật để xài thử.",
        "Vừa update {update} trong repo. Thêm tính năng mới theo feedback.",
    ],
}

# === TOPIC DATA ===
TOPICS = {
    "segment analysis": "phân nhóm user theo behavior trước khi launch campaign",
    "retention": "giữ chân user không phải là gửi nhiều notification",
    "voucher design": "thiết kế offer theo segment, không phải ai cũng thích giảm giá",
    "A/B testing": "chạy A/B test đủ sample trước khi kết luận",
    "campaign planning": "lên kế hoạch campaign từ target ra hành động",
    "MEU planning": "lên campaign từ target MEU, không phải từ budget",
    "brief writing": "viết brief 5 input ra 1 trang, không phải 10 trang",
    "production review": "review agent trước khi chạy campaign thật",
}

RESULTS = [
    "tỷ lệ click tăng 40% sau 2 tuần",
    "chi phí giảm 30% so với campaign trước",
    "thời gian phân tích từ 3 tiếng xuống 15 phút",
    "tỷ lệ reactivate đạt 12%, gấp 3 lần campaign manual",
]

UPDATES = [
    "thêm hỗ trợ OpenAI provider",
    "cập nhật context system",
    "fix bug A/B Test Analyzer",
    "thêm example output mới",
    "cập nhật prompt cho agent mới",
]


def get_week_of_month():
    """Tính tuần trong tháng (1-4)"""
    today = datetime.now()
    return (today.day - 1) // 7


def get_schedule():
    """Xác định pillar + agent cho hôm nay"""
    today = datetime.now()
    weekday = today.weekday()  # 0=Mon
    week = get_week_of_month()
    pillar, tag = PILLARS.get(weekday, ("Nghỉ", "#nghi"))

    result = {"pillar": pillar, "tag": tag, "agent": None}

    if pillar == "Agent Demo":
        # Chọn agent theo rotation
        rotation_agents = WEEK_ROTATION[week % 4]
        agent_idx = 0 if weekday in (1,) else 1  # T2 or T5
        agent_id = rotation_agents[agent_idx % 2]
        result["agent"] = next(a for a in AGENTS if a["folder"] == agent_id)
        result["topic_title"] = result["agent"]["title"]

    elif pillar == "Growth Tip":
        import random
        keys = list(TOPICS.keys())
        key = keys[(today.day + weekday) % len(keys)]
        result["topic_title"] = key
        result["topic_desc"] = TOPICS[key]

    elif pillar == "Case Study":
        import random
        keys = list(TOPICS.keys())
        key = keys[(today.day) % len(keys)]
        result["topic_title"] = key
        result["result"] = RESULTS[(today.day) % len(RESULTS)]

    elif pillar == "Repo Update":
        import random
        result["update"] = UPDATES[(today.day) % len(UPDATES)]

    return result


def generate_hooks(schedule):
    """Sinh hook ideas dựa trên pillar"""
    pillar = schedule["pillar"]
    templates = HOOKS.get(pillar, [])
    hooks = []

    for t in templates[:2]:
        hook = t
        if pillar == "Agent Demo" and schedule.get("agent"):
            hook = hook.replace("{agent}", schedule["agent"]["title"])
            hook = hook.replace("{desc}", schedule["agent"]["desc"])
        elif pillar == "Growth Tip" and schedule.get("topic_title"):
            hook = hook.replace("{topic}", schedule["topic_title"])
        elif pillar == "Case Study":
            hook = hook.replace("{topic}", schedule.get("topic_title", "growth"))
            hook = hook.replace("{result}", schedule.get("result", "tốt hơn"))
        elif pillar == "Repo Update":
            hook = hook.replace("{update}", schedule.get("update", "nội dung mới"))
        hooks.append(hook)

    return hooks


def send_telegram(text):
    """Gửi gợi ý content qua Telegram"""
    if not TELEGRAM_TOKEN:
        print(f"[Telegram disabled] {text[:100]}...")
        return
    import requests
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
    )


def run():
    schedule = get_schedule()
    hooks = generate_hooks(schedule)

    # Build message
    lines = [f"💡 GỢI Ý CONTENT — hôm nay ({datetime.now().strftime('%d/%m')})"]
    lines.append(f"\n📌 Pillar: {schedule['pillar']}")

    if schedule.get("agent"):
        a = schedule["agent"]
        lines.append(f"\n📁 Agent: {a['title']}")
        lines.append(f"   {a['desc']}")
        lines.append(f"   Folder: {a['folder']}")

    if schedule.get("topic_title"):
        lines.append(f"\n📝 Chủ đề: {schedule['topic_title']}")
        if schedule.get("topic_desc"):
            lines.append(f"   {schedule['topic_desc']}")

    if schedule.get("result"):
        lines.append(f"   Kết quả tham khảo: {schedule['result']}")

    if schedule.get("update"):
        lines.append(f"\n📦 Update: {schedule['update']}")

    lines.append(f"\n✏️ Hook ideas:")
    for i, h in enumerate(hooks, 1):
        lines.append(f"  {i}. {h}")

    lines.append(f"\n📎 github.com/thaolst/ai-growth-agents-for-marketers")

    msg = "\n".join(lines)
    print(msg)
    send_telegram(msg)
    return msg


if __name__ == "__main__":
    run()
