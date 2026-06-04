"""
Skills module — modular capabilities for Growth Orchestrator
Each skill is a standalone Python file with a run() function

CowAgent-inspired: modular, single-responsibility, pluggable
ZeroClaw-inspired: SOPs, approval gates

Available skills:
    scan.py     — Quét cấu trúc repo, tìm gaps
    develop.py  — Tạo prompt + SKILL.md mới
    example.py  — Thêm ví dụ output vào README
    content.py  — Viết bài LinkedIn/Facebook/Threads
    analyze.py  — Phân tích content performance

Usage:
    from skills import scan
    result = scan.run("/path/to/repo")
"""
