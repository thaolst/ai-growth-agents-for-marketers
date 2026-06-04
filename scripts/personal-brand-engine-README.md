# Personal Brand Engine — AI Agent cho Marketer

![version](https://img.shields.io/badge/version-2.0.0-4ade80?style=flat-square) ![type](https://img.shields.io/badge/type-personal-brand-60a5fa?style=flat-square) [![← repo](https://img.shields.io/badge/←_back-repo-a78bfa?style=flat-square)](../README.md)

**Automated personal brand builder for marketers.**  
Develop GitHub repos → Auto-generate social content → Track performance → Top 1 SEA.

## Why This Exists

Bạn là marketer có expertise thực tế nhưng không có thời gian xây personal brand?

Vấn đề:
1. Phát triển nội dung chất lượng tốn thời gian
2. Duy trì đều đặn mỗi ngày khó
3. Content cho 3 nền tảng (LinkedIn, Facebook, Threads) khác nhau
4. Không biết cái gì đang chạy tốt, cần điều chỉnh gì

Giải pháp: Agent này tự động:
- Quét repo GitHub hằng ngày, đề xuất nội dung cần phát triển
- Sinh bài đăng cho 3 platform với tone riêng
- Track hiệu quả, ưu tiên chủ đề chạy tốt
- Gate: bạn duyệt trước khi public

## Flow Hằng Ngày

```
19:30 GitHub Actions → Gợi ý task qua Telegram
      ↓
Bạn duyệt hoặc đề xuất task khác
      ↓
Thực thi → Push GitHub → Sinh content 3 kênh
      ↓
Bạn duyệt → Đăng LinkedIn / Facebook / Threads
```

## Tính Năng

| Tính năng | Mô tả |
|-----------|-------|
| 🧠 **Bộ nhớ** | Nhớ chủ đề đã làm, content nào chạy tốt, không lặp |
| 🗺️ **Lộ trình** | Roadmap theo tuần, ưu tiên repo có tác động cao nhất |
| 📊 **GitHub API** | Track stars, forks, commits real-time |
| 📝 **Content AI** | Tự động viết LinkedIn, Facebook, Threads theo tone riêng |
| 🎯 **Mục tiêu Top 1 SEA** | Theo dõi tiến trình đến 100★ |
| 🔒 **Approval Gate** | Bạn duyệt trước mọi public action |

## Skills Module (Modular)

```
scripts/skills/
├── scan.py      — Quét cấu trúc repo, tìm gaps
├── develop.py   — Tạo prompt + SKILL.md mới
├── example.py   — Thêm ví dụ output vào README
└── content.py   — Viết bài cho LinkedIn, Facebook, Threads
```

Mỗi skill là 1 file Python độc lập. Thêm skill mới không cần sửa core engine.

## Sử dụng

```bash
# Gợi ý task mỗi tối
python3 scripts/growth-engine.py daily

# Chạy task đã duyệt
python3 scripts/growth-engine.py execute agents "Build Campaign Monitor Agent"

# Gọi skill riêng
python3 -c "from skills import scan; print(scan.run('path/to/repo'))"
```

## Mục tiêu

**Top 1 AI x Growth Marketing GitHub repo tại SEA (2026 Q3)**

| Mốc | Trạng thái |
|-----|-----------|
| 10★ — Early adopters | ✅ Prompts đạt 8★ |
| 50★ — Regional recognition | 🔄 Đang tiến hành |
| 100★ — Top 1 SEA | 🎯 Mục tiêu |
| 500★ — Global awareness | 🚀 Tương lai |

## Tech Stack

- Python 3.11+
- GitHub REST API
- Telegram Bot API
- GitHub Actions (cron scheduling)
