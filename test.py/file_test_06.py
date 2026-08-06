# ========================================
print(f"\n{"=" * 40}\n")

# 실습6. CSV 읽어 조건 저장하기
print("실습6. CSV 읽어 조건 저장하기")

# CSV를 읽어 조건에 맞는 데이터만 골라 새 CSV로 저장하기

#   ① csv를 import

#   ② csv.reader로 읽고 첫 줄 헤더는 건너뛰기

#   ③ 값을 float로 변환해 기준(90) 초과 행만 리스트에 모으기

#   ④ csv.writer로 모은 행들을 새 CSV에 저장


# ========================================
print(f"\n{"=" * 40}\n")


# ① csv 모듈을 import

import csv

filtered_data = []

# ② csv.reader로 읽고 첫 줄 헤더는 건너뛰기
with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    # ③ 값을 float로 변환해 기준(90) 초과 행만 리스트에 모으기
    for row in reader:
        current = float(row[4])

        if current > 90:
            filtered_data.append(row)

# ④ csv.writer로 모은 행들을 새 CSV에 저장
with open("result_filter.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(header)

    for row in filtered_data:
        writer.writerow(row)
