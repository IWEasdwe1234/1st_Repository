# == 실습 1. 데이터 불러오기와 구조 확인하기 ==
print("== 실습 1. 데이터 불러오기와 구조 확인하기 ==")

import pandas as pd

# 목표
# 설비 센서 CSV를 불러와 크기와 열 이름 확인

# 단계
# read_csv로 설비 센서 파일 불러오기
df_small = pd.read_csv("data/13_diecasting_small.csv")

# head로 앞부분, shape로 행·열 크기 확인

print("\n[df_small.head() 출력]\n")
print(df_small.head())

print("\n[df_small.shape 출력]\n")
print(df_small.shape)

print(f"\n{"-"*40}\n")

# columns로 열 이름 목록 확인

print("[df_small.columns 출력]\n")
print(df_small.columns)
