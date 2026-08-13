# == 실습 2. 열 선택하기 ==
print("== 실습 2. 열 선택하기 ==")

import pandas as pd

# 목표
# 한 열(Series)과 여러 열(DataFrame)을 선택하고 바로 계산

# 단계

# data/13_diecasting_small.csv 파일 열기
df = pd.read_csv("data/13_diecasting_small.csv")

# 대괄호 한 겹으로 단일 열을 Series로 선택
# : '형체력' 컬럼 하나만 빼오기
print('\ndf["형체력"] 출력\n')
print(df["형체력"])

# ----------------------------------------
print(f"\n{"-"*40}\n")

# 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
# '형체력', '실린더압력' 두개를 선택하기
print('df[["형체력", "실린더압력"]] 출력\n')
print(df[["형체력", "실린더압력"]])

# ----------------------------------------
print(f"\n{"-"*40}\n")

# 선택한 열에 mean으로 평균 계산
# df['형체력'].mean() -> round로 소숙점 이하 1자리까지만 나오게 조정해주세요
print('round(df["형체력"].mean(), 1) 출력\n')
print(round(df["형체력"].mean(), 1))
