# ========================================
print(f"\n{"=" * 40}\n")

# 실습5. csv.writer로 csv 쓰기
print("실습5. csv.writer로 csv 쓰기")

#   ① csv 모듈을 import

#   ② with open으로 w·utf-8·newline 옵션으로 열기

#   ③ csv.reader로 writer 객체를 만들기

#   ④ writerow로 헤더와 각 데이터 행을 쓰기

# ========================================
print(f"\n{"=" * 40}\n")


# ① csv 모듈을 import

import csv

# ② with open으로 w·utf-8·newline 옵션으로 열기
with open("result.csv", "w", encoding="utf-8", newline="") as f:

    # ③ csv.reader로 writer 객체를 만들기
    writer = csv.writer(f)

    #   ④ writerow로 헤더와 각 데이터 행을 쓰기
    writer.writerow(["시각", "설비"])
    writer.writerow(["14:30", "PUMP-02"])
