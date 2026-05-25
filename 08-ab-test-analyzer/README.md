# A/B Test Analyzer

Mình chạy A/B test thường xuyên nhưng phần mất thời gian nhất không phải là chạy test — là đọc kết quả và quyết định xem kết quả đó có đủ tin cậy không, winner thực sự là cái nào, và nên làm gì tiếp theo.

Agent này nhận raw data từ A/B test, tự tính statistical significance, xác định winner, và quan trọng hơn — giải thích tại sao và đề xuất bước tiếp theo bằng ngôn ngữ không cần biết thống kê mới hiểu.

## Những gì mình hay nhầm trước khi dùng agent này

Nhìn vào conversion rate cao hơn và tuyên bố winner — mà không kiểm tra sample size có đủ không. Kết quả nhiều lần bị flip sau khi chạy thêm vài ngày.

Kết luận test không có kết quả khi thực ra là cần chạy thêm thời gian. Agent tính được cần bao nhiêu sample nữa để có kết luận đáng tin.

Bỏ qua segment breakdown — đôi khi variant A win overall nhưng variant B lại win rõ ràng với một segment cụ thể, và đó mới là insight quan trọng hơn.

## Kết quả thực tế

Từ 3 tiếng đọc kết quả và viết báo cáo xuống còn 15 phút. Phần lớn thời gian tiết kiệm được là từ việc không phải tra Google "how to calculate statistical significance" mỗi lần.


# English

I run A/B tests regularly but the most time-consuming part isn't running the test — it's reading the results and deciding whether they're reliable, which variant actually won, and what to do next.

This agent takes raw A/B test data, calculates statistical significance, identifies the winner, and — most importantly — explains why and recommends next steps in language you don't need a statistics background to understand.

## What I used to get wrong before using this agent

Declaring a winner just because the conversion rate was higher — without checking if sample size was sufficient. Results flipped multiple times after running for a few more days.

Concluding a test was inconclusive when it actually needed more time to run. The agent calculates exactly how much more sample or time is needed for a reliable conclusion.

Ignoring segment breakdowns — sometimes variant A wins overall but variant B clearly wins with a specific segment, and that's the more important insight.

## Real result

From one day to read results and write a report down to 15 minutes. Most of the time saved is from not having to Google "how to calculate statistical significance" every time.
