# SOPs — Standard Operating Procedures

> Inspired by ZeroClaw: approval gates, tool receipts, audit trails
> Version: 1.0 — 04/06/2026

## SOP-001: DAILY FLOW

**When:** 19:30 GMT+7 (GitHub Actions) + manual trigger anytime

**Steps:**
1. **SCAN** — Quét cả 2 repos (prompts + agents)
2. **MEMORY CHECK** — Không đề xuất task đã làm trong 3 ngày gần nhất
3. **PROPOSE** — Gửi 1 task + 1 content hook qua Telegram
4. **APPROVAL** — Chờ Thảo OK. Nếu 30' không reply → skip ngày đó
5. **EXECUTE** — Thực thi task đã duyệt
6. **PUSH** — Commit message format: `[type]: [summary]`
7. **CONTENT** — Sinh bài từ nội dung vừa push

**Approval Gate:** Step 4 + Step 6 đều cần Thảo duyệt

---

## SOP-002: TASK PROPOSE

**Rules:**
1. agents repo (weight 3) > prompts repo (weight 2)
2. Ưu tiên task có tác động cao đến star count
3. Không đề xuất task trùng với 3 ngày gần nhất
4. Nếu roadmap có task pending cho tuần này → ưu tiên

**Format:**
```
🎯 HÔM NAY:
  Repo: [repo name]
  Task: [task description]
  Lý do: [vì sao chọn task này]
  ⏱ Effort: [ước lượng thời gian]
  📈 Impact: [tác động lên star/content]
```

---

## SOP-003: PUSH GATE

**Rules:**
1. Commit message format:
   - `feat:` — tính năng mới
   - `docs:` — documentation
   - `fix:` — sửa lỗi
   - `refactor:` — cải thiện code
   - `chore:` — maintenance
2. Không push file chứa token/secret
3. Push xong → update memory → sinh content
4. Nếu push lỗi → báo Thảo + rollback

---

## SOP-004: CONTENT

**Rules:**
1. Content chỉ từ nội dung **vừa push**, không invent
2. 1 link duy nhất / bài (đến folder cụ thể, không root repo)
3. Tone theo platform:
   - **LinkedIn:** Chuyên sâu, hook pain point → giải pháp → CTA
   - **Facebook:** Kể chuyện cá nhân, casual
   - **Threads:** Cực ngắn, 1-2 câu
4. Platform-specific format:
   - LinkedIn hook: "Là Growth Marketing, phần mình thấy nhiều người hiểu sai nhất về..."
   - Facebook: "Hồi mới làm...", "Chuyện là..."
   - Threads: 1 câu + link

---

## SOP-005: MEMORY

**Data stored:**
```
dev_log: [{date, repo, action, topic, status}]
content_log: [{date, platform, topic, link}]
performance: {topic: {views, likes, comments, date}}
roadmap_progress: {week: {planned, done, skipped}}
```
**Rules:**
1. Giữ tối đa 50 entries gần nhất cho dev_log
2. Performance chỉ lưu khi Thảo cung cấp số liệu
3. Memory dùng để tránh lặp + ưu tiên chủ đề chạy tốt

---

## SOP-006: ROADMAP

**Current goal:** Top 1 AI x Growth Marketing GitHub tại SEA (2026 Q3)

**Milestones:**
```
10★  → Early adopters     (prompts đã 8★)
50★  → Regional recognition
100★ → Top 1 SEA (target)
500★ → Global awareness
```

**Priority weights:**
- agents repo: 3 (phát triển agent mới + social proof)
- prompts repo: 2 (ví dụ output + glossary + trending)

**Weekly review:** Chủ nhật → review progress + adjust roadmap
