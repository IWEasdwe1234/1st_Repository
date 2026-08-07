# ========================================
print(f"\n{"="*40}\n")

# 실습 4. 불량 방어
print("실습 4. 불량 방어")

# 실습목표
# · 불량 데이터를 걸러내고, 범위 밖 값은 raise 로 차단한다.
# 앞서 배운 모든 예외처리 기법을 총동원한다.

# 만들어야 할 것
# 온도를 처리하며 숫자로 못 바꾸는 값과 정상 범위를 벗어난 값을 모두 걸러낸다.
# 불량 줄은 번호와 이유를 함께 기록한다.

# 한 함수에 모이는 것들
# try-except · continue · raise · as e 가 한 함수에 모두 들어간다.
# 앞서 배운 게 여기서 총정리된다.

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

# ---------------------------------------
print(f"\n{"-"*40}\n")
print("[실습 2 - 재사용]\n")

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

# ---------------------------------------
print(f"\n{"-"*40}\n")
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

# ========================================
print(f"\n{"="*40}\n")
print("[실습 4 - 불량 방어]\n")


def check_temperature(rows, index):
    bad_rows = []

    for number, row in enumerate(rows, start=1):

        try:
            temp = float(row[index])
            high = float(row[4])
            low = float(row[5])

            if temp > high or temp < low:
                raise ValueError("정상 범위 초과")

        except ValueError as e:
            bad_rows.append((number, str(e)))
            continue

        except IndexError as e:
            bad_rows.append((number, "데이터 열 부족"))
            continue

    return bad_rows


# 불량 데이터 검사 실행
bad_rows = check_temperature(rows, 2)

print("\n불량 데이터 목록")

for number, reason in bad_rows:
    print(f"{number}번째 행 : {reason}")
