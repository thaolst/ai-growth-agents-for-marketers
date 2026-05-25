# Example output — Script kéo data tự động

Input: mỗi tuần kéo data từ file CSV, tính conversion rate theo segment, xuất ra file mới.
Script được tạo ra:

```python
# Script tính conversion rate theo segment từ file CSV
# Chạy: python agent.py

import pandas as pd
import os
from datetime import datetime

# Đường dẫn file input — đổi thành đường dẫn file của bạn
INPUT_FILE = "campaign_data.csv"
OUTPUT_FOLDER = "reports"

def tinh_conversion_rate(df):
    # Tính conversion rate = số conversion / số impression, theo từng segment
    ket_qua = df.groupby('segment').agg(
        total_users=('user_id', 'count'),
        total_conversions=('converted', 'sum')
    ).reset_index()
    
    ket_qua['conversion_rate'] = (ket_qua['total_conversions'] / ket_qua['total_users'] * 100).round(2)
    return ket_qua

def chay():
    # Kiểm tra file có tồn tại không
    if not os.path.exists(INPUT_FILE):
        print(f"Lỗi: Không tìm thấy file {INPUT_FILE}")
        print("Kiểm tra lại đường dẫn file")
        return
    
    # Đọc file
    print(f"Đang đọc {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)
    
    # Tính kết quả
    ket_qua = tinh_conversion_rate(df)
    
    # Tạo folder output nếu chưa có
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Lưu file với tên có ngày tháng
    ten_file = f"{OUTPUT_FOLDER}/conversion_report_{datetime.now().strftime('%Y%m%d')}.csv"
    ket_qua.to_csv(ten_file, index=False)
    
    # In tóm tắt
    print(f"\nXong! Kết quả lưu tại: {ten_file}")
    print(f"\nTóm tắt:")
    print(ket_qua.to_string(index=False))

if __name__ == "__main__":
    chay()
```

Hướng dẫn chạy lần đầu:

Mở Terminal (Mac: Command + Space, gõ "Terminal"). Di chuyển đến folder chứa script: `cd đường-dẫn-folder`. Cài thư viện cần thiết: `pip install pandas`. Đặt file CSV của bạn cùng folder với script, đổi tên thành `campaign_data.csv` hoặc sửa dòng `INPUT_FILE` trong script. Chạy: `python agent.py`.


# English

Input: pull data from a CSV file weekly, calculate conversion rate by segment, export to a new file.

The script created does the following: reads a CSV file, groups by segment, calculates conversion rate for each, saves a dated output file, and prints a summary to the terminal. Estimated time saved: from 45 minutes of manual work down to running one command.
