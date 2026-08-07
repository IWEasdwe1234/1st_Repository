# ========================================
print(f"\n{"="*40}\n")

# 실습 2. 조건 분류
print("실습 2. 조건 분류")

# 만들어야 할 것
# 1단계 데이터를 설비별로 분류
# 각 설비에 몇 개의 데이터가 있는지 출력한다.
# 딕셔너리의 키는 설비명, 값은 행 리스트다.

# 핵심 패턴
# 처음 보는 설비명이면 빈 리스트를 먼저 만들고, 거기에 행을 추가하는 방식이다.

# ========================================
print(f"\n{"="*40}\n")
print("[실습 1 - 재사용]\n")

import csv


def read_csv_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader)
            rows = list(reader)

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

        return [], []


file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv_file(file_path)

print("헤더 : ", header)
print("데이터 행 수 :", len(rows))

# ========================================
print(f"\n{"="*40}\n")
print("[실습 2]\n")

equipment_data = {}

for row in rows:

    # 딕셔너리 키(설비명)
    equipment = row[1]

    # 처음 보는 설비명이면 빈 리스트 생성
    if equipment not in equipment_data:

        # 딕셔너리 값(행 리스트)
        equipment_data[equipment] = []

    # 빈 리스트에 데이터 추가
    equipment_data[equipment].append(row)

print("\n설비별 데이터 개수")

for equipment, data in equipment_data.items():
    print(f"{equipment} : {len(data)}개")
