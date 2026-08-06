# ========================================
print(f"\n{"=" * 40}\n")

# 실습4. csv.reader로 csv 읽기
print("실습4. csv.reader로 csv` 읽기")

#   ① csv 모듈을 import

#   ② with open으로 CSV를 읽기 모드 utf-8로 열기

#   ③ csv.reader로 reader 객체를 만들기

#   ④ for로 각 행(리스트)을 하나씩 꺼내 출력

# ========================================
print(f"\n{"=" * 40}\n")


# ① csv 모듈을 import

import csv
import os

csv_path = os.path.join("data", "08_press.csv")

# ② with open으로 CSV를 읽기 모드 utf-8로 열기
with open(csv_path, "r", encoding="utf-8") as f:

    # ③ csv.reader로 reader 객체를 만들기
    reader = csv.reader(f)

    # ④ for로 각 행(리스트)을 하나씩 꺼내 출력
    for row in reader:
        print(row)
