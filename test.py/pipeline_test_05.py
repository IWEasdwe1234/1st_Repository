# ========================================
print(f"\n{"="*40}\n")

# 실습 5. 리포트 저장
print("실습 5. 리포트 저장")

# 실습목표
# · 분석 결과를 리포트 형식으로 정리해 txt 파일로 저장
# 핵심 요약은 위, 세부 통계는 구분선 아래.

# 만들어야 할 것
# 4단계까지의 결과를 리포트 형식으로 정리해 txt 파일에 저장
# 저장 후 파일을 다시 열어 내용을 직접 확인

# 작성 방식
# 리포트 줄들을 리스트에 차곡차곡 모은 뒤, 마지막에 반복문으로 한 번에 파일에 쓴다.

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

# ---------------------------------------
print(f"\n{"-"*40}\n")
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

# ========================================
print(f"\n{"="*40}\n")
print("[실습 5 - 리포트 저장]\n")

# 리포트 내용 저장 리스트
report_lines = []


# 리포트 제목
report_lines.append("센서 검사 리포트\n")
report_lines.append("=" * 40 + "\n")


# 핵심 요약
report_lines.append("[핵심요약]\n")

report_lines.append(f"전체 데이터 수 : {len(rows)}개\n")
report_lines.append(f"불량 데이터 수 : {len(bad_rows)}개\n")

# 구분선
report_lines.append("\n" + "=" * 40 + "\n")


# 측정값 통계
report_lines.append("\n[측정값 통계]\n")

if result is not None:
    count, avg, minimum, maximum = result

    report_lines.append(f"개수 : {count}\n")
    report_lines.append(f"평균 : {round(avg, 2)}\n")
    report_lines.append(f"최솟값 : {minimum}\n")
    report_lines.append(f"최댓값 : {maximum}\n")
else:
    report_lines.append("계산할 데이터가 없습니다.\n")

# 설비별 데이터 개수
report_lines.append("\n[설비별 데이터 개수]\n")

for equipment, data in equipment_data.items():
    report_lines.append(f"{equipment} : {len(data)}개\n")


# 불량 데이터 목록
report_lines.append("\n[불량 데이터 목록]\n")

for number, reason in bad_rows:
    report_lines.append(f"{number}번째 행 : {reason}\n")


# 리포트 저장
import os

os.makedirs("data", exist_ok=True)

report_file = "data/inspection_report.txt"

with open(report_file, "w", encoding="utf-8") as f:

    for line in report_lines:
        f.write(line)

print("\n리포트 저장 완료:", report_file)


# 저장된 리포트 확인
print("\n저장된 리포트 내용\n")

with open(report_file, "r", encoding="utf-8") as f:
    report = f.read()

print(report)
