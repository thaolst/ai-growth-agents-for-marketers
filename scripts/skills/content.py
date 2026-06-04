"""
Skill: Write social content for LinkedIn, Facebook, Threads
Generates platform-appropriate posts from a task description
"""
import json

def run(task, repo_link):
    """Generate 3 posts from task context
    
    Returns: {linkedin: str, facebook: str, threads: str}
    """
    topic = task.get("topic", task.get("task", ""))
    repo = task.get("repo", "agents")
    
    if "prompt" in repo or "prompts" in repo:
        repo_name = "ai-growth-prompts"
    else:
        repo_name = "ai-growth-agents-for-marketers"
    
    link = f"github.com/thaolst/{repo_name}"
    if repo_link:
        link = repo_link
    
    linkedin = (
        f"Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về {topic} là "
        f"nghĩ nó quá phức tạp.\n\n"
        f"Thực ra mình đã đóng gói kinh nghiệm thực tế vào repo GitHub, "
        f"ai làm growth có thể dùng luôn.\n\n"
        f"Vừa public free, ghé thử nghiệm ngay.\n\n"
        f"{link}"
    )
    
    facebook = (
        f"Mất bao lâu để hiểu {topic}? Mình mất 3 năm campaign thực tế, "
        f"rồi code lại thành prompt trong repo.\n\n"
        f"Mới update trên GitHub, free cho ai cần.\n\n"
        f"{link}"
    )
    
    threads = (
        f"{topic}. Đã code thành prompt, public free trên GitHub.\n\n"
        f"{link}"
    )
    
    return {"linkedin": linkedin, "facebook": facebook, "threads": threads}
