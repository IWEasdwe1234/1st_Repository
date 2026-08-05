# ========================================
print("\n" + "=" * 40 + "\n")

# 실습 3.os로 폴더 목록 살펴보기
print("실습 3.os로 폴더 목록 살펴보기")

# os로 현재 위치를 확인하고 폴더 안 파일 목록을 순회하기

# 단계
#   ① os 모듈을 import

#   ② getcwd로 현재 작업 폴더를 확인

#   ③ listdir로 폴더 안 목록을 변수에 담기

#   ④ for로 목록을 하나씩 출력하고 csv만 골라 출력

# ========================================
print("\n" + "=" * 40 + "\n")

# ① os 모듈을 import
print("① 모듈을 import\n")

import os

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ② getcwd로 현재 작업 폴더를 확인
print("② getcwd로 현재 작업 폴더를 확인\n")
current_working_directory = os.getcwd()
print(current_working_directory)  # C:\Users\PC2510\Desktop\1st_Repository

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ③ listdir로 폴더 안 목록을 변수에 담기
print("③ listdir로 폴더 안 목록을 변수에 담기\n")

file_list = os.listdir()

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ④ for로 목록을 하나씩 출력하고 csv만 골라 출력
print("④ for로 목록을 하나씩 출력하고 csv만 골라 출력\n")

for file_name in file_list:
    print(file_name)
