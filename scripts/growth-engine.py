"""
Growth Engine — Agent trung tâm phát triển GitHub cho Thảo
Định hướng Top 1 AI x Growth Marketing tại SEA
Memory + Roadmap + GitHub API + Social + Priority Engine
"""
import json, os, sys, re, random, subprocess
from datetime import datetime, timedelta
from urllib.request import Request, urlopen
from urllib.error import URLError

# === CONFIG ===
ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT, "growth-engine-config.json")
default_cfg = {
    "repos": {
        "prompts": "~/Developer/ai-growth-prompts",
        "agents": "~/Developer/ai-growth-agents-for-marketers"
    },
    "telegram_chat_id": "1606915846",
    "telegram_token_env": "TELEGRAM_BOT_TOKEN",
    "github_user": "thaolst"
}
try:
    with open(CONFIG_PATH) as f:
        user_cfg = {k: v for k, v in json.load(f).items()
                    if not str(v).startswith("YOUR_")}
    CFG = {**default_cfg, **user_cfg}
except:
    CFG = default_cfg

for k in CFG.get("repos", {}):
    CFG["repos"][k] = os.path.expanduser(CFG["repos"][k])

MEMORY_DIR = os.path.join(ROOT, "memory")
os.makedirs(MEMORY_DIR, exist_ok=True)
ROADMAP_PATH = os.path.join(ROOT, "roadmap.json")
TELEGRAM_TOKEN = os.environ.get(CFG["telegram_token_env"], "")

# === GITHUB INTEGRATION ===
class GitHubAPI:
    """Fetch public GitHub data for tracking + gap analysis"""

    def __init__(self):
        self.user = CFG.get("github_user", "thaolst")

    def _fetch(self, url):
        try:
            req = Request(url, headers={"User-Agent": "growth-engine"})
            with urlopen(req, timeout=10) as r:
                return json.loads(r.read())
        except: return None

    def repo_stats(self, repo_name):
        """Get stars, forks, last updated"""
        data = self._fetch(f"https://api.github.com/repos/{self.user}/{repo_name}")
        if data:
            return {
                "stars": data.get("stargazers_count", 0),
                "forks": data.get("forks_count", 0),
                "open_issues": data.get("open_issues_count", 0),
                "updated": data.get("pushed_at", ""),
                "description": data.get("description", "")
            }
        return {"stars": 0, "forks": 0}

    def recent_commits(self, repo_name, days=7):
        """Get commit count in last N days"""
        data = self._fetch(f"https://api.github.com/repos/{self.user}/{repo_name}/commits?per_page=30")
        if not data: return 0
        cutoff = datetime.now() - timedelta(days=days)
        count = 0
        for c in data:
            date_str = c.get("commit", {}).get("committer", {}).get("date", "")
            if date_str:
                try:
                    d = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                    if d > cutoff: count += 1
                except: pass
        return count

    def compare_sea_peers(self, repo_name):
        """Compare Thảo's repo vs SEA competitors in AI x Growth"""
        peers = {
            "ai-growth-prompts": [
                ("kdn251", "interviews"),   # placeholder — real SEA peers
                ("trungdq88", "Awesome-Startup-Tools"),
            ],
            "ai-growth-agents-for-marketers": [
                ("techtalk-sg", "ai-marketing-agents"),
            ]
        }
        stats = self.repo_stats(repo_name)
        peer_data = []
        for owner, rname in peers.get(repo_name, []):
            d = self._fetch(f"https://api.github.com/repos/{owner}/{rname}")
            if d:
                peer_data.append({"name": rname, "stars": d.get("stargazers_count", 0)})
        return {"mine": stats.get("stars", 0), "peers": peer_data}


# === PRIORITY MAP ===
REPO_PRIORITY = {
    "agents": {
        "weight": 3,
        "label": "ai-growth-agents-for-marketers",
        "focus": "Xây agents mới + social proof cho agents hiện có",
        "topics": ["Campaign Monitor Agent", "Xu Economy Agent", "Experiment Tracker"]
    },
    "prompts": {
        "weight": 2,
        "label": "ai-growth-prompts",
        "focus": "Thêm minh hoạ + mở rộng glossary + trending update",
        "topics": ["Ví dụ output cho folder 00-08", "Glossary VI mở rộng", "Trending July"]
    }
}

SEA_TARGET = {
    "goal": "Top 1 AI x Growth Marketing GitHub repo tại SEA (2026 Q3)",
    "target_stars": 100,
    "target_followers": 50,
    "milestones": [
        {"stars": 10, "label": "Early adopters"},
        {"stars": 50, "label": "Regional recognition"},
        {"stars": 100, "label": "Top 1 SEA (mục tiêu)"},
        {"stars": 500, "label": "Global awareness"},
    ]
}


# ==================== MEMORY SYSTEM ====================
class Memory:
    def __init__(self):
        self.path = os.path.join(MEMORY_DIR, "engine.json")
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {
            "dev_log": [],           # [{date, repo, action, topic, status}]
            "content_log": [],       # [{date, platform, topic, link}]
            "performance": {},       # {topic: {views, likes, comments}}
            "roadmap_progress": {},  # {week: {planned, done, skipped}}
            "daily_plan": [],        # queue các task
            "last_repo_update": {}   # {repo: date}
        }

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def log_dev(self, repo, action, topic, status="done"):
        self.data["dev_log"].append({
            "date": datetime.now().isoformat(),
            "repo": repo, "action": action,
            "topic": topic, "status": status
        })
        self.data["last_repo_update"][repo] = datetime.now().isoformat()
        self.save()

    def log_content(self, platform, topic):
        self.data["content_log"].append({
            "date": datetime.now().isoformat(),
            "platform": platform, "topic": topic
        })
        self.save()

    def update_performance(self, topic, views, likes, comments):
        self.data["performance"][topic] = {"views": views, "likes": likes, "comments": comments}
        self.save()

    def get_recent_dev(self, days=3):
        cutoff = datetime.now() - timedelta(days=days)
        return [e for e in self.data["dev_log"]
                if datetime.fromisoformat(e["date"]) > cutoff]

    def get_best_performers(self, n=3):
        perf = self.data.get("performance", {})
        sorted_perf = sorted(perf.items(), key=lambda x: x[1].get("likes", 0), reverse=True)
        return [p[0] for p in sorted_perf[:n]]


# ==================== ROADMAP ====================
class Roadmap:
    """Lộ trình phát triển theo tuần, ưu tiên repo có weight cao hơn"""

    def __init__(self, memory: Memory):
        self.mem = memory
        self.data = self._load()

    def _load(self):
        if os.path.exists(ROADMAP_PATH):
            with open(ROADMAP_PATH) as f:
                return json.load(f)
        return self._default_roadmap()

    def _default_roadmap(self):
        today = datetime.now()
        week_num = today.isocalendar()[1]
        return {
            "current_week": week_num,
            "goal": "Top 1 AI x Growth Marketing trên GitHub (2026 Q3)",
            "weeks": {
                str(week_num): {
                    "focus": "Setup growth engine + content pipeline",
                    "tasks": [
                        {"repo": "agents", "task": "Hoàn thiện content-suggester v2", "status": "done"},
                        {"repo": "agents", "task": "Setup GitHub Actions cron", "status": "done"},
                        {"repo": "prompts", "task": "Thêm ví dụ output folder 00-08", "status": "pending"},
                    ]
                },
                str(week_num + 1): {
                    "focus": "Agent mới + Social proof",
                    "tasks": [
                        {"repo": "agents", "task": "Build Campaign Monitor Agent", "status": "pending"},
                        {"repo": "agents", "task": "Viết case study cho 3 agents", "status": "pending"},
                    ]
                },
                str(week_num + 2): {
                    "focus": "Xu Economy + Community",
                    "tasks": [
                        {"repo": "agents", "task": "Build Xu Economy Agent", "status": "pending"},
                        {"repo": "prompts", "task": "Update trending July + glossary", "status": "pending"},
                    ]
                }
            }
        }

    def save(self):
        with open(ROADMAP_PATH, "w") as f:
            json.dump(self.data, f, indent=2)

    def today_task(self):
        """Xác định task hôm nay: dựa trên roadmap + priority + memory"""
        week = str(self.data.get("current_week", datetime.now().isocalendar()[1]))
        tasks = self.data.get("weeks", {}).get(week, {}).get("tasks", [])

        # Ưu tiên task chưa làm
        pending = [t for t in tasks if t["status"] == "pending"]
        if pending:
            # Ưu tiên repo có weight cao hơn
            pending.sort(key=lambda t: REPO_PRIORITY.get(t["repo"], {}).get("weight", 1), reverse=True)
            return pending[0]

        # Nếu hết task tuần này → đề xuất từ priority
        for repo_key, info in sorted(REPO_PRIORITY.items(), key=lambda x: x[1]["weight"], reverse=True):
            recent = self.mem.get_recent_dev(3)
            last_done = [e for e in recent if e["repo"] == repo_key]
            if len(last_done) < 2:  # Chưa làm nhiều
                return {"repo": repo_key, "task": info["focus"], "topic": info["topics"][0]}

        return {"repo": "prompts", "task": "Mở rộng nội dung", "topic": "Thêm ví dụ output"}


# ==================== REPO SCANNER ====================
class RepoScanner:
    def scan(self, repo_path):
        """Scan repo, lấy danh sách folders + file count"""
        if not os.path.exists(repo_path):
            return {"error": "not found"}
        folders = []
        for item in sorted(os.listdir(repo_path)):
            fpath = os.path.join(repo_path, item)
            if not os.path.isdir(fpath) or item.startswith("."):
                continue
            files = [f for f in os.listdir(fpath) if not f.startswith(".")]
            has_readme = "README.md" in files
            has_skill = "SKILL.md" in files
            folders.append({"name": item, "files": len(files), "has_readme": has_readme, "has_skill": has_skill})
        return {"folders": folders, "total": len(folders)}


# ==================== SOCIAL SUGGESTER ====================
class SocialPrompter:
    def suggest_post(self, task):
        """Gợi ý bài đăng từ task vừa làm"""
        repo = task.get("repo", "agents")
        info = REPO_PRIORITY.get(repo, {})
        topic = task.get("topic", task.get("task", ""))
        label = info.get("label", repo)

        hooks = [
            f"Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {topic} là...",
            f"Mình vừa cập nhật {topic} trong repo. Cách nó giúp tiết kiệm thời gian hơn tưởng tượng.",
        ]
        return {
            "pillar": "Agent Demo" if "agent" in topic.lower() else "Growth Tip",
            "hook_ideas": hooks,
            "link": f"github.com/thaolst/{label}",
            "topic": topic
        }


# ==================== GROWTH ENGINE ====================
class GrowthEngine:
    def __init__(self):
        self.mem = Memory()
        self.roadmap = Roadmap(self.mem)
        self.scanner = RepoScanner()
        self.social = SocialPrompter()
        self.tg_token = TELEGRAM_TOKEN
        self.tg_chat = CFG.get("telegram_chat_id", "")

    def _telegram(self, text):
        if self.tg_token and self.tg_chat:
            import requests
            requests.post(f"https://api.telegram.org/bot{self.tg_token}/sendMessage",
                          data={"chat_id": self.tg_chat, "text": text, "parse_mode": "HTML"})

    def daily(self):
        """Flow 1 ngày: GitHub Stats → Scan → Plan → Suggest → Chờ duyệt"""
        today = datetime.now().strftime("%d/%m/%Y")
        lines = [f"🤖 GROWTH ENGINE — {today}", ""]

        gh = GitHubAPI()

        # === B0: GitHub Stats ===
        lines.append(f"🎯 MỤC TIÊU: Top 1 AI x Growth SEA ({SEA_TARGET['target_stars']}★)")
        for repo_key in ["agents", "prompts"]:
            label = REPO_PRIORITY[repo_key]["label"]
            stats = gh.repo_stats(label)
            commits = gh.recent_commits(label, 7)
            lines.append(f"  {label}: {stats.get('stars',0)}★ {stats.get('forks',0)}⑂ · {commits} commits/7d")
        lines.append("")

        # === B1: Scan ===
        lines.append("📊 SCAN REPO:")
        for repo_key, repo_path in CFG["repos"].items():
            result = self.scanner.scan(repo_path)
            if "error" in result:
                lines.append(f"  ❌ {repo_key}: {result['error']}")
            else:
                lines.append(f"  ✅ {repo_key}: {result['total']} folders")
        lines.append("")

        # === B2: Check memory ===
        recent = self.mem.get_recent_dev(3)
        if recent:
            lines.append("📝 GẦN ĐÂY ĐÃ LÀM:")
            for e in recent:
                lines.append(f"  • {e['topic']} ({e['repo']}) — {e['status']}")
            lines.append("")

        # === B3: Performance ===
        best = self.mem.get_best_performers(2)
        if best:
            lines.append(f"🔥 CHẠY TỐT NHẤT: {', '.join(best)}")
            lines.append("")

        # === B4: Task hôm nay ===
        task = self.roadmap.today_task()
        # Topic fallback
        topic = task.get("topic") or task.get("task", "Phát triển nội dung")
        repo_key = task.get("repo", "agents")
        label = REPO_PRIORITY.get(repo_key, {}).get("label", repo_key)
        focus = REPO_PRIORITY.get(repo_key, {}).get("focus", "")
        lines.append(f"🎯 HÔM NAY:")
        lines.append(f"  Repo: {repo_key} ({label})")
        lines.append(f"  Focus: {focus}")
        lines.append(f"  Task: {topic}")
        lines.append("")

        # === B5: Social ===
        post = self.social.suggest_post(task)
        lines.append(f"📝 GỢI Ý CONTENT:")
        for h in post.get("hook_ideas", []):
            lines.append(f"  • {h}")
        lines.append(f"  🔗 {post.get('link', '')}")
        lines.append("")

        lines.append("⚠️ Cần Thảo duyệt trước khi phát triển.")
        lines.append("Reply OK để bắt đầu, hoặc gợi ý task khác.")

        msg = "\n".join(lines)
        print(msg)
        self._telegram(msg)
        return task

    def execute(self, task):
        """Thực thi task sau khi duyệt — chạy script tương ứng"""
        repo = task["repo"]
        topic = task.get("topic", task.get("task", ""))
        print(f"🚀 Executing: {repo} → {topic}")

        # Tuỳ task type, chạy script phù hợp
        if repo == "agents":
            # Chạy repo-dev-agent để scan + suggest
            import subprocess
            result = subprocess.run(
                ["python3", os.path.join(ROOT, "repo-dev-agent.py"), "scan"],
                capture_output=True, text=True, timeout=30
            )
            print(result.stdout)
        elif repo == "prompts":
            print(f"📝 Cần phát triển prompts: {topic}")

        self.mem.log_dev(repo, "develop", topic, "done")
        print("✅ Done — chờ Thảo duyệt trước push")


if __name__ == "__main__":
    engine = GrowthEngine()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "daily"

    if cmd == "daily":
        engine.daily()
    elif cmd == "execute":
        # Load task từ stdin hoặc args
        task = json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {
            "repo": sys.argv[2] if len(sys.argv) > 2 else "agents",
            "task": sys.argv[3] if len(sys.argv) > 3 else "Phát triển nội dung",
            "topic": sys.argv[4] if len(sys.argv) > 4 else "Nội dung mới"
        }
        engine.execute(task)
    else:
        print("Usage: python3 growth-engine.py [daily|execute]")
