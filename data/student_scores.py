# ========================================
print(f"\n{"="*40}\n")

# 학생들의 점수를 가져와서
# 각 학생별 합계와
# 모든 학생들의 평균 점수를 내는 코드

# 1. 파일을 연다
# 2. 파일 내용으로부터 리스트 데이터를 얻는다
# 3. 점수 계산
# 4. 결과를 화면에 보여주기

# ========================================

import os
import sys
import csv

# 0. 미리 전체 합산 점수 낼 준비를 한다
total_all = 0
students_count = 0

# 1. 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

with open(file_path, "r", encoding="utf-8") as f:

    # 2. 파일 내용으로부터 리스트 데이터를 얻는다
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        total = (kor + eng + math) / 3
        print(
            f"[{name}] 국어 : {kor} | 영어 : {eng} | 수학 : {math} | 평균 : {round(total,2)}"
        )

        # 3. 점수 계산 (합계, 합산)
        students_count += 1
        total_all += total

# 4. 결과를 화면에 보여주기
avg_all = total_all / students_count
print(f"\n전체 : {students_count}명 | 평균 : {round(avg_all,2)}점")

# ========================================
print(f"\n{"="*40}\n")


# [제출 안하는 실습]
# student_score.py를 기반으로
# 1. 실행 끝날 때 최고점 학생, 최저점 학생도 찾아서 출력해보세요
# 2. 실행 끝날 때 각 과목별 평균도 출력해보세요 (선택)

# 1:50 까지


import os
import sys
import csv

total_all = 0
total_kor = 0
total_eng = 0
total_math = 0
students_count = 0


max_score = 0
max_student = ""
max_result = {}

min_score = 100
min_student = ""
min_result = {}


file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

with open(file_path, "r", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        total = (kor + eng + math) / 3

        # 최고점
        if total > max_score:
            max_score = total
            max_student = name
            max_result = {"국어": kor, "영어": eng, "수학": math}

        # 최저점
        if total < min_score:
            min_score = total
            min_student = name
            mix_result = {"국어": kor, "영어": eng, "수학": math}

        print(
            f"[{name}] 국어 : {kor} | 영어 : {eng} | 수학 : {math} | 평균 : {round(total,2)}"
        )

        students_count += 1
        total_all += total
        total_kor += total
        total_eng += total
        total_math += total


avg_all = total_all / students_count
avg_kor = total_kor / students_count
avg_eng = total_eng / students_count
avg_math = total_math / students_count

print(f"\n전체 : {students_count}명 | 평균 : {round(avg_all, 2)}점")

print(f"최고점 : {max_student} | 평균 : {round(max_score, 2)}")
print(f"최저점 : {min_student} | 평균 : {round(min_score, 2)}")

print(f"모든 학생 국어 평균 {round(avg_kor,2)}")
print(f"모든 학생 영어 평균 {round(avg_eng,2)}")
print(f"모든 학생 수학 평균 {round(avg_math,2)}")

print(f"최고점 : {max_student}")
print(f"국어 : {max_result['국어']}")
print(f"영어 : {max_result['영어']}")
print(f"수학 : {max_result['수학']}")
print(f"평균 : {round(max_score, 2)}")
