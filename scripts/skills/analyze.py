"""
Skill: Analyze content performance + suggest improvements
Dùng để track bài nào chạy tốt, điều chỉnh chiến lược
"""
import json, os
from datetime import datetime

def run(performance_data=None):
    """Phân tích performance data và đưa ra suggest
    
    Args:
        performance_data: dict {topic: {views, likes, comments, date}}
    """
    if not performance_data:
        # Load từ memory nếu có
        mem_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "memory", "engine.json")
        if os.path.exists(mem_path):
            with open(mem_path) as f:
                mem = json.load(f)
            performance_data = mem.get("performance", {})
    
    if not performance_data:
        return {
            "status": "no_data",
            "message": "Chưa có performance data. Thảo cung cấp sau khi đăng bài.",
            "suggestions": ["Đăng bài → note lại likes/comments → gửi em"]
        }
    
    # Phân tích
    total = len(performance_data)
    best_topic = max(performance_data.items(), key=lambda x: x[1].get("likes", 0)) if performance_data else None
    avg_likes = sum(d.get("likes", 0) for d in performance_data.values()) / total if total > 0 else 0
    
    result = {
        "status": "ok",
        "total_topics": total,
        "avg_likes": round(avg_likes, 1),
        "best_topic": best_topic[0] if best_topic else None,
        "best_likes": best_topic[1].get("likes", 0) if best_topic else 0,
        "suggestions": []
    }
    
    if best_topic:
        result["suggestions"].append(f"🔥 Chủ đề chạy tốt nhất: \"{best_topic[0]}\" — {best_topic[1].get('likes', 0)} likes")
        result["suggestions"].append("→ Phát triển thêm nội dung liên quan đến chủ đề này")
    
    if avg_likes < 10:
        result["suggestions"].append("📉 Average likes thấp. Thử: hook mạnh hơn, CTA rõ hơn, post vào khung giờ khác")
    
    return result
