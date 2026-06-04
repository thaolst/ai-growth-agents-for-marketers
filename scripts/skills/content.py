"""
Skill: Write personal brand content cho marketer
3 platforms: LinkedIn (chuyên sâu), Facebook (kể chuyện), Threads (ngắn)
Dùng winning format từ Thảo: Hook pain point → giải pháp → CTA
"""
import json

# Template library từ content đã chạy tốt
TEMPLATES = {
    "linkedin": {
        "repo_update": [
            'Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {topic} là nghĩ nó quá phức tạp.\n\nThực ra {solution}. Mình đã đóng gói kinh nghiệm thực tế vào repo, ai cần thì dùng luôn.\n\n{detail}\n\nVừa public free trên GitHub, ai làm growth thì thử nghiệm ngay.\n\n{link}',
            'Mình vừa update {topic} trên GitHub.\n\n{problem}\n\nTrong repo có {solution}.\n\n{detail}\n\n{link}'
        ],
        "agent_demo": [
            'Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {topic} là...\n\nThực ra {topic} chỉ là trả lời {question_count} câu hỏi:\n{questions}\n\nMình dùng {agent_name} trong repo để tự động hoá việc này. {solution}\n\nKhông cần mở Excel, không cần tính tay.\n\nVừa public free trên GitHub, ai làm growth có {target} thì thử nghiệm ngay.\n\n{link}'
        ]
    },
    "facebook": {
        "story": [
            'Hồi mới làm {topic}, mất cả {time_period} để {pain}. Lần nào cũng sợ {fear}.\n\nGiờ có {solution}. {value_prop}\n\nMất {time_learn} để hiểu, mất {time_build} để code, tiết kiệm {time_save}.\n\nRepo để trên GitHub free, ai làm growth thì ghé thử.\n\n{link}'
        ]
    },
    "threads": {
        "short": [
            '{topic}. {one_liner}\n\n{link}',
            '3 câu hỏi để {goal}:\n{questions}\n\n{link}'
        ]
    }
}

def run(task, repo_link):
    """Generate 3 platform-specific posts
    
    Returns: {linkedin: str, facebook: str, threads: str}
    """
    topic = task.get("topic", task.get("task", ""))
    repo = task.get("repo", "agents")
    
    if "prompt" in repo:
        repo_name = "ai-growth-prompts"
    else:
        repo_name = "ai-growth-agents-for-marketers"
    
    link = repo_link or f"github.com/thaolst/{repo_name}"
    
    # === LINKEDIN ===
    linkedin = (
        f"Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {topic} "
        f"là nghĩ nó quá phức tạp.\n\n"
        f"Thực ra mình đã đóng gói kinh nghiệm thực tế vào repo GitHub, "
        f"ai làm growth có thể dùng luôn mà không cần nghĩ nhiều.\n\n"
        f"Prompt kèm ví dụ output cụ thể, copy paste vào campaign của mình được ngay.\n\n"
        f"Vừa public free trên GitHub, ai làm growth thì thử nghiệm ngay.\n\n"
        f"{link}"
    )
    
    # === FACEBOOK (kể chuyện, personal) ===
    facebook = (
        f"Hồi mới vào growth, mình lụi prompt template trên mạng về rồi tự hỏi "
        f"\"output ra sao nhỉ\". Mất cả buổi để chỉnh sửa cho vừa campaign.\n\n"
        f"Giờ mình viết hết vào repo GitHub — có prompt + ví dụ output thật, "
        f"copy paste là chạy. Ai làm growth marketing mà muốn tiết kiệm thời gian "
        f"thì ghé thử, free.\n\n"
        f"{link}"
    )
    
    # === THREADS (cực ngắn) ===
    threads = (
        f"{topic}. Đã đóng gói thành prompt + ví dụ output, "
        f"public free trên GitHub. Copy paste chạy luôn.\n\n"
        f"{link}"
    )
    
    return {"linkedin": linkedin, "facebook": facebook, "threads": threads}
