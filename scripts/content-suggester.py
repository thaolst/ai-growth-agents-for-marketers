#!/usr/bin/env python3
"""
Content Suggester v2 — với Session + Memory (Day 3 from Kaggle)
Nhớ chủ đề đã gợi ý, không lặp lại trong 7 ngày.
Memory persist ra file JSON.
"""
import json, os, sys, random
from datetime import datetime, timedelta

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "1606915846")
MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", ".content-memory.json")

# === AGENTS ===
AGENTS = [
    {"id": "01", "title": "AI Agent Consultant", "desc": "Tư vấn chọn agent phù hợp", "has_code": False},
    {"id": "02", "title": "Campaign Brief Agent", "desc": "5 input sang brief hoàn chỉnh", "has_code": False},
    {"id": "03", "title": "Campaign Synthesis", "desc": "Tổng hợp nhiều file campaign", "has_code": False},
    {"id": "04", "title": "Automation Scripter", "desc": "Tự viết Python script", "has_code": True},
    {"id": "05", "title": "Multi-Agent Pipeline", "desc": "Research ra Planning", "has_code": True},
    {"id": "06", "title": "Agentic RAG", "desc": "Hỏi đáp từ campaign history", "has_code": False},
    {"id": "07", "title": "Planning Agent", "desc": "Target sang campaign plan", "has_code": True},
    {"id": "08", "title": "A/B Test Analyzer", "desc": "Phân tích và đề xuất", "has_code": True},
    {"id": "09", "title": "MEU Planning Agent", "desc": "MEU target sang campaign plan", "has_code": True},
    {"id": "10", "title": "Production Review", "desc": "Review agent trước deploy", "has_code": True},
]

PILLARS = {0: "Growth Tip", 1: "Agent Demo", 2: "Growth Tip", 3: "Agent Demo",
           4: "Growth Tip", 5: "Agent Demo", 6: "Repo Update"}
WEEK_ROTATION = [["02", "09"], ["08", "07"], ["06", "03"], ["04", "10"]]
TOPICS = [
    "segment analysis", "retention", "voucher design", "A/B testing",
    "campaign planning", "MEU planning", "brief writing", "production review"
]
HOOK_TEMPLATES = {
    "Agent Demo": [
        "Hôm nay mình dùng {agent}. Cách nó {desc}, khác hẳn làm tay.",
        "Mình vừa thử {agent} cho campaign tuần này.",
    ],
    "Growth Tip": [
        "Phần mình thấy nhiều người hiểu sai nhất về {topic} là nghĩ nó phức tạp.",
        "Mẹo nhỏ: {topic}. Áp dụng AI agent vào việc này nhanh hơn bạn nghĩ.",
    ],
    "Repo Update": [
        "Tuần này repo có thêm gì mới: {update}.",
        "Vừa cập nhật {update} theo feedback.",
    ],
}

# === MEMORY SYSTEM (Day 3: Sessions & Memory) ===

class MemoryStore:
    """Persistent memory — nhớ chủ đề đã gợi ý, tracking frequency, tránh lặp"""

    def __init__(self, path=MEMORY_FILE):
        self.path = path
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {"suggested_topics": [], "posted_topics": [],
                "agent_frequency": {}, "last_run": None, "session_count": 0}

    def _save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def is_recent(self, topic, days=7):
        """Check if topic was suggested in last N days"""
        cutoff = datetime.now() - timedelta(days=days)
        for t in self.data["suggested_topics"]:
            if t["topic"] == topic:
                ts = datetime.fromisoformat(t["timestamp"])
                if ts > cutoff:
                    return True
        return False

    def mark_suggested(self, topic):
        self.data["suggested_topics"].append(
            {"topic": topic, "timestamp": datetime.now().isoformat()})
        self.data["session_count"] += 1
        self.data["last_run"] = datetime.now().isoformat()
        # Track agent frequency
        for agent in AGENTS:
            if agent["title"] == topic or agent["id"] == topic:
                key = agent["id"]
                self.data["agent_frequency"][key] = self.data["agent_frequency"].get(key, 0) + 1
                break
        self._save()

    def get_top_agents(self, n=3):
        """Return most frequently suggested agents — để biết content nào chạy tốt"""
        sorted_by_freq = sorted(
            self.data["agent_frequency"].items(), key=lambda x: x[1], reverse=True)
        return [a for a, f in sorted_by_freq[:n]]

    def get_least_used_agent(self):
        """Return agent with least suggestions — để ưu tiên content mới"""
        freq = self.data["agent_frequency"]
        least = min(AGENTS, key=lambda a: freq.get(a["id"], 0))
        return least


# === SELECTION LOGIC (rút gọn) ===

def get_schedule(memory):
    today = datetime.now()
    weekday = today.weekday()
    week = (today.day - 1) // 7
    pillar = PILLARS.get(weekday, "Nghỉ")

    result = {"pillar": pillar}

    if pillar == "Agent Demo":
        rotation = WEEK_ROTATION[week % 4]
        # Ưu tiên agents chưa được suggest
        least = memory.get_least_used_agent()
        if least["id"] not in rotation:
            rotation[-1] = least["id"]
        agent_id = rotation[0] if weekday in (1, 5) else rotation[1]
        result["agent"] = next(a for a in AGENTS if a["id"] == agent_id)
        result["topic"] = result["agent"]["title"]

    elif pillar == "Growth Tip":
        # Tránh topic đã suggest gần đây
        available = [t for t in TOPICS if not memory.is_recent(t)]
        result["topic"] = random.choice(available) if available else random.choice(TOPICS)

    elif pillar == "Repo Update":
        updates = ["thêm OpenAI provider", "cập nhật context system",
                   "fix bug A/B Test Analyzer", "thêm example output mới"]
        result["update"] = random.choice(updates)

    return result


def generate_hooks(schedule):
    templates = HOOK_TEMPLATES.get(schedule["pillar"], [])
    hooks = []
    for t in templates[:2]:
        if schedule["pillar"] == "Agent Demo" and schedule.get("agent"):
            t = t.replace("{agent}", schedule["agent"]["title"])
            t = t.replace("{desc}", schedule["agent"]["desc"])
        elif schedule["pillar"] == "Growth Tip":
            t = t.replace("{topic}", schedule.get("topic", "growth"))
        elif schedule["pillar"] == "Repo Update":
            t = t.replace("{update}", schedule.get("update", "nội dung mới"))
        hooks.append(t)
    return hooks


def send_telegram(text):
    """Day 3: check memory trước khi gửi — nếu topic đã gửi hôm nay thì skip"""
    if not TELEGRAM_TOKEN:
        print(f"[Local] {text[:80]}...")
        return
    import requests
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                  data={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"})


def run():
    memory = MemoryStore()
    schedule = get_schedule(memory)

    # Check memory: tránh lặp
    topic = schedule.get("topic", schedule.get("update", ""))
    if memory.is_recent(topic):
        print(f"⏭️ {topic} đã suggest gần đây, skip")
        return

    hooks = generate_hooks(schedule)

    lines = [f"💡 GỢI Ý CONTENT — {datetime.now().strftime('%d/%m')}"]
    lines.append(f"\n📌 Pillar: {schedule['pillar']}")
    lines.append(f"📝 {schedule.get('topic', schedule.get('update', ''))}")

    if schedule.get("agent"):
        a = schedule["agent"]
        lines.append(f"📁 {a['id']} — {a['title']}")

    lines.append(f"\n✏️ Hook:")
    for h in hooks:
        lines.append(f"  • {h}")

    lines.append(f"\n📎 github.com/thaolst/ai-growth-agents-for-marketers")
    if schedule.get("agent"):
        lines.append(f"  /tree/main/{schedule['agent']['id']}-meu-planning-agent")

    msg = "\n".join(lines)
    print(msg)

    # Ghi memory trước khi gửi
    memory.mark_suggested(topic)
    send_telegram(msg)

    # Day 4: Observability log
    print(f"\n📊 [Observability] Session #{memory.data['session_count']}")
    print(f"   Topic: {topic} | Pillar: {schedule['pillar']}")
    print(f"   Memory size: {len(memory.data['suggested_topics'])} entries")

    return msg


if __name__ == "__main__":
    run()
