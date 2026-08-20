# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
print(ln)
# 실습 2. SECOM 첫 탐색 -> 사출성형_공정.csv
print("실습 2. SECOM 첫 탐색사출성형_공정.csv")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# head·shape·info·describe로 결측 분위기 파악

import pandas as pd

df = pd.read_csv("data/15_01_사출성형_공정.csv", encoding="utf-8")
# 목표
# 처음 받은 데이터의 구조와 결측 분위기 파악

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# read_csv로 불러와 head와 shape로 크기 확인
print("==[ head와 shape ]==\n")
print("--[ head ]--\n")
print(df.head())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

print("--[ shape ]--\n")
print(df.shape)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# info로 컬럼별 채워진 값 개수 훑기
print("==[ info ]==\n")
df.info()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# describe의 count로 결측 있는 컬럼 짐작
print("==[ describe ]==\n")
print(df.describe())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
