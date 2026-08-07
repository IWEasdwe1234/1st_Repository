# ========================================
print(f"\n{"="*40}\n")

# 실습 3. 통계 함수
print("실습 3. 통계 함수")

# 실습목표
# 평균 · 최대 · 최소를 계산하는 함수를 만든다.
# 함수로 만들어 어떤 데이터에도 재사용할 수 있게 한다.

# 만들어야 할 것
# 특정 칸의 숫자 데이터로 개수, 평균, 최솟값, 최댓값을 계산하는 함수.

# 주의할 점
# 숫자가 아닌 값은 건너뛴다.
# · 값이 하나도 없으면 None을 반환해 0으로 나누는 오류를 막는다.

# ========================================
print(f"\n{"="*40}\n")
print("[실습 1 - CSV 읽기]\n")

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

# ---------------------------------------
print(f"\n{"-"*40}\n")
print("[실습 2 - 조건 분류]\n")

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

# ========================================
print(f"\n{"="*40}\n")
print("[실습 3 - 통계 함수]\n")


def calculate_stats(rows, index):
    values = []

    for row in rows:
        try:
            value = float(row[index])
            values.append(value)

        # 숫자가 아닌 값 건너 뛰기
        except ValueError:
            continue

    # 숫자 데이터가 없으면 None을 반환
    if len(values) == 0:
        return None

    # 개수, 평균, 최솟값, 최댓값
    count = len(values)
    avg = sum(values) / count
    minimum = min(values)
    maximum = max(values)

    return count, avg, minimum, maximum


# 측정값(index 2) 통계 계산
result = calculate_stats(rows, 2)

print("\n측정값 통계")

if result is None:
    print("계산할 데이터가 없습니다.")

else:
    count, avg, minimum, maximum = result

    print("개수", count)
    print("평균", round(avg, 2))
    print("최솟값", minimum)
    print("최댓값", maximum)
