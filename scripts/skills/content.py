"""
Skill: Write personal brand content cho marketer — nâng cấp
Format chuẩn cho từng kênh: LinkedIn / Facebook / Threads
"""
import random

# ==================== LINKEDIN FORMAT ====================
# Cấu trúc: Hook (1 câu) → Context (2-3 câu) → Detail (bullet) → CTA (1 câu) → Link
# Tone: Professional nhưng personal, data-driven, storytelling
# Dài: 200-400 từ, 4-5 đoạn ngắn

HOOKS_LINKEDIN = [
    # 1. Pain point hook (winning format)
    lambda t: f"Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {t} là nghĩ nó quá phức tạp.",
    # 2. Question hook
    lambda t: f"Bạn đã bao giờ mất cả buổi để {t}?",
    # 3. Story hook
    lambda t: f"3 tháng trước mình ngồi Excel tính tay {t}. 3 tháng sau mình code hết thành prompt.",
    # 4. Insight hook
    lambda t: f"Điều mình học được sau nhiều năm làm growth: {t} không cần hoàn hảo ngay từ đầu.",
    # 5. Contrast hook
    lambda t: f"Trước: mất 3 ngày để {t}. Sau: mất 3 phút cho AI chạy, 30 phút review."
]

BODY_LINKEDIN = [
    lambda h, t: f"{h}\n\nMình cũng từng vật lộn với việc này. Cho đến khi mình nhận ra: vấn đề không phải thiếu kiến thức, mà là thiếu template để bắt đầu.\n\nMình bắt đầu ghi lại tất cả prompt đang dùng hằng ngày, kèm ví dụ output thực tế. Kết quả: giảm 70% thời gian làm campaign, focus vào đúng phần quan trọng.",
    lambda h, t: f"{h}\n\nSự thật là: {t} chỉ cần 3 thứ — framework đúng, data sạch, và template có sẵn. Phần còn lại là AI lo.\n\nMình public luôn bộ template đang dùng, ai cần thì lấy về dùng.",
    lambda h, t: f"{h}\n\nCách mình giải quyết: viết prompt template cho từng bước trong quy trình. Mỗi prompt kèm scenario thật + output kỳ vọng. Copy paste vào campaign của mình là chạy được ngay, không cần điều chỉnh nhiều."
]

CTA_LINKEDIN = [
    "Vừa public free trên GitHub, ai làm growth thì thử nghiệm ngay.",
    "Link repo bên dưới, ai cần thì copy về dùng.",
    "GitHub free, fork về chạy thử rồi cho mình biết feedback nhé."
]

def _linkedin_post(topic, link):
    hook = random.choice(HOOKS_LINKEDIN)(topic)
    body = random.choice(BODY_LINKEDIN)(hook, topic)
    cta = random.choice(CTA_LINKEDIN)
    return f"{body}\n\n{cta}\n\n{link}"


# ==================== FACEBOOK FORMAT ====================
# Cấu trúc: Story opening (1-2 câu) → Problem (2 câu) → Resolution (1-2 câu) → CTA nhẹ → Link
# Tone: Như kể chuyện với bạn, personal, có emoji nhẹ nhàng
# Dài: 100-200 từ

STORY_OPENINGS = [
    lambda t: f"Hồi mới vào growth, mình cứ nghĩ {t} là phải ngồi Excel tính tay. Mất cả buổi, sai vài chỗ là làm lại từ đầu.",
    lambda t: f"Chuyện là tuần trước mình ngồi 2 tiếng để {t}. Bực mình quá, mình code luôn cái prompt cho việc này.",
    lambda t: f"Hồi đó mất 3 ngày để làm {t}. Giờ 3 phút là xong. Sự khác biệt nằm ở chỗ có template sẵn hay không.",
    lambda t: f"Mình thấy nhiều bạn growth marketing giỏi nhưng mất thời gian vào {t}. Việc lặp lại mà, có template là xong."
]

STORY_RESOLUTIONS = [
    lambda t: f"Giờ có prompt template sẵn rồi. Nhập số liệu campaign, AI chạy, mình chỉ review. Tiết kiệm thời gian, focus vào phần quan trọng hơn.",
    lambda t: f"Giờ chỉ cần copy prompt trong repo, paste vào, đổi số liệu campaign — xong. Đơn giản hơn mình tưởng rất nhiều.",
    lambda t: f"Code hết vào GitHub rồi. Có prompt + ví dụ output, ai cần thì dùng, free."
]

FACEBOOK_LINKS = [
    lambda link: f"Link repo đây, ai cần thì ghé: {link}",
    lambda link: f"Repo để free trên GitHub: {link}",
    lambda link: f"{link}"
]

def _facebook_post(topic, link):
    opening = random.choice(STORY_OPENINGS)(topic)
    resolution = random.choice(STORY_RESOLUTIONS)(topic)
    link_text = random.choice(FACEBOOK_LINKS)(link)
    return f"{opening}\n\n{resolution}\n\n{link_text}"


# ==================== THREADS FORMAT ====================
# Cấu trúc: 4-5 câu conversational + link
# Tone: Tự nhiên, như đang nói chuyện, storytelling nhẹ
# Dài: 4-5 câu (~200-300 ký tự)

THREADS_CONTENT = [
    lambda t, l: f"{t} là việc mình từng mất cả buổi để làm. Cho đến khi mình code hết thành prompt template.\n\nGiờ chỉ cần copy, paste, đổi số liệu — chạy luôn. Tiết kiệm thời gian kinh khủng.\n\nRepo free trên GitHub, ai cần thì ghé.\n\n{l}",
    lambda t, l: f"Mình thấy nhiều người làm growth vẫn đang tự làm {t} từ đầu mỗi lần. Tốn thời gian lắm.\n\nMình public luôn bộ prompt template đang dùng. Có ví dụ output cụ thể, copy paste vào campaign là chạy được ngay.\n\n{l}",
    lambda t, l: f"Hồi mới làm growth, {t} là việc mình sợ nhất. Mất cả buổi, sai vài chỗ là làm lại.\n\nGiờ có template rồi. Nhập số liệu, AI chạ�y, mình chỉ review.\n\nAi cần thì lấy về dùng, free.\n\n{l}",
    lambda t, l: f"3 tháng trước mình ngồi Excel tính tay {t}. 3 tháng sau code hết thành prompt.\n\nTiết kiệm 2 ngày làm việc mỗi tháng. Work smarter, not harder.\n\nRepo GitHub free cho ai cần.\n\n{l}",
    lambda t, l: f"Bạn đã bao giờ mất cả buổi để {t}? Mình cũng từng vậy.\n\nCho đến khi mình viết prompt template cho việc này. Có scenario thật + output kỳ vọng. Copy paste chạy luôn.\n\nFree trên GitHub, ai làm growth thì thử.\n\n{l}"
]

def _threads_post(topic, link):
    return random.choice(THREADS_CONTENT)(topic, link)


# ==================== MAIN ====================
def run(task, repo_link):
    topic = task.get("topic", task.get("task", ""))
    repo = task.get("repo", "prompts")
    
    link = repo_link or (f"github.com/thaolst/ai-growth-prompts" if "prompt" in repo else "github.com/thaolst/ai-growth-agents-for-marketers")
    
    return {
        "linkedin": _linkedin_post(topic, link),
        "facebook": _facebook_post(topic, link),
        "threads": _threads_post(topic, link)
    }
