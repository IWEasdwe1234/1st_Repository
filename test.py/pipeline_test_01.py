# ========================================
print(f"\n{"="*40}\n")

# 실습 1. CSV 읽기
print("실습 1. CSV 읽기")

# 만들어야 할 것
# data/09_ict_inspection_dirty.csv 를 읽어 헤더와 데이터 행을 분리
# 데이터가 몇 행인지 출력하는 함수를 만든다.
# 함수로 만들어 이후 단계에서 그대로 재사용한다.

# 예외 처리
# 파일이 없는 경우 FileNotFoundError가 발생한다.
# 안내 메시지를 출력한 뒤 빈 결과(빈 header, 빈 rows)를 반환하도록 한다.

# ========================================
print(f"\n{"="*40}\n")

import csv


def read_csv_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            # 헤더 분리
            header = next(reader)

            # 데이터 행 분리
            rows = list(reader)

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

        # 빈 결과 반환
        return [], []


file_path = "data/09_ict_inspection_dirty.csv"

header, rows = read_csv_file(file_path)

print("헤더 : ", header)
print("데이터 행 수 :", len(rows))
