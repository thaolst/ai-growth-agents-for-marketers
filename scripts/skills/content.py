"""
Skill: Write personal brand content cho marketer
5+ hooks khác nhau, không lặp template
"""
import random

HOOKS_LINKEDIN = [
    # Hook dạng pain point
    lambda t: f"Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {t} là nghĩ nó quá phức tạp.\n\nThực ra mình đã đóng gói kinh nghiệm thực tế vào repo GitHub.\n\n{_detail(t)}\n\nVừa public free trên GitHub, ai làm growth thì thử nghiệm ngay.",
    
    # Hook dạng câu hỏi
    lambda t: f"Bạn đã bao giờ mất cả buổi để {t}?\n\nMình cũng từng như vậy. Cho đến khi mình code hết vào GitHub — có prompt + ví dụ output, copy paste chạy luôn.\n\n{_detail(t)}\n\n{_link()}",
    
    # Hook dạng story ngắn
    lambda t: f"3 tháng trước mình ngồi Excel tính tay {t}. 3 tháng sau mình viết hết thành prompt trên GitHub.\n\nTiết kiệm 2 ngày làm việc mỗi tháng. Đúng nghĩa work smarter.\n\n{_detail(t)}\n\n{_link()}",
    
    # Hook dạng insight
    lambda t: f"Điều mình học được sau nhiều năm làm growth: {t} không cần phải hoàn hảo ngay từ đầu. Quan trọng là có template để bắt đầu.\n\nMình public luôn prompt đang dùng hằng ngày trên GitHub.\n\n{_link()}",
    
    # Hook dạng comparison
    lambda t: f"Trước: mất 3 ngày để làm {t}.\nSau: mất 3 phút để AI chạy, 30 phút để review.\n\nSự khác biệt nằm ở prompt template có sẵn. Mình để trong repo, free.\n\n{_link()}"
]

HOOKS_FACEBOOK = [
    lambda t: f"Hồi mới làm growth, mình cứ nghĩ {t} là phải ngồi Excel tính tay. Mất cả buổi, sai vài chỗ là làm lại từ đầu.\n\nGiờ code hết vào prompt template trên GitHub rồi. Nhập số liệu, AI chạy, mình chỉ review.\n\nTiết kiệm thời gian, focus vào phần quan trọng hơn.\n\nFree trên GitHub, ai cần thì ghé.",
    lambda t: f"Chuyện là hồi tháng trước mình ngồi 2 tiếng để {t}. Bực mình quá, mình code luôn cái agent tự động làm việc này.\n\nGiờ chạy 30 giây là xong. Cả repo public free, ai muốn dùng thì clone về.\n\n{_link()}",
    lambda t: f"Mình thấy nhiều bạn growth marketing giỏi nhưng mất thời gian vào việc lặp lại. {t} là một trong những việc đó.\n\nMình viết prompt cho những việc này rồi, để trong repo free. Copy paste paste là chạy.\n\n{_link()}"
]

HOOKS_THREADS = [
    lambda t: f"{t}. Prompt template free trên GitHub. Copy paste chạy luôn.",
    lambda t: f"Mất {random.choice(['2 ngày', '3 buổi', '1 tuần'])} để làm {t}? Mất 30 giây với AI. Repo free:",
    lambda t: f"Growth marketers: đừng tự làm {t} từ đầu nữa. Dùng prompt có sẵn.",
    lambda t: f"{t}. Code hết vào GitHub rồi. Ai cần thì dùng, free."
]

def _detail(t):
    details = [
        "Prompt kèm ví dụ output cụ thể, copy paste vào campaign của mình được ngay.",
        "Có scenario thật + output kỳ vọng, áp dụng luôn vào campaign đang chạy.",
        "Không lý thuyết suông — tất cả đều đã kiểm chứng qua campaign thực tế.",
    ]
    return random.choice(details)

def _link():
    links = [
        "github.com/thaolst/ai-growth-prompts",
        "github.com/thaolst/ai-growth-agents-for-marketers"
    ]
    return random.choice(links)

def run(task, repo_link):
    topic = task.get("topic", task.get("task", ""))
    repo = task.get("repo", "prompts")
    
    link = repo_link or (f"github.com/thaolst/ai-growth-prompts" if "prompt" in repo else "github.com/thaolst/ai-growth-agents-for-marketers")
    
    # Chọn hook ngẫu nhiên, không lặp
    linkedin = random.choice(HOOKS_LINKEDIN)(topic)
    facebook = random.choice(HOOKS_FACEBOOK)(topic)
    threads = random.choice(HOOKS_THREADS)(topic)
    
    # Đảm bảo link xuất hiện trong bài
    if link not in linkedin:
        linkedin += f"\n\n{link}"
    if link not in facebook:
        facebook += f"\n\n{link}"
    if link not in threads:
        threads += f"\n\n{link}"
    
    return {"linkedin": linkedin, "facebook": facebook, "threads": threads}
