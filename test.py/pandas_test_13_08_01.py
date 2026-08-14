# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 1. 단일 조건으로 행 추출하기")
# 실습 1. 단일 조건으로 행 추출하기

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 목표
# 조건을 만들고 그 조건으로 원하는 행만 추출

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
print("== df.info() 실행 ==\n")
df.info()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 단계
# 비교 연산자로 실린더압력 기준의 조건식을 만들어 Boolean Series 생성

s = df["실린더압력"]

s_boolean = s >= 230
print("== s_boolean.info() 출력 ==\n")
s_boolean.info()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# sum으로 조건을 만족하는 행 개수 확인
print("== s_boolean.sum() 출력 ==\n")
print(s_boolean.sum())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 만든 조건을 데이터프레임 대괄호에 넣어 행 추출
df_sub = df[df["실린더압력"] >= 230]
print("== df_sub.info() 실행 ==\n")
df_sub.info()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
