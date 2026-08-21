# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
print(ln)

print("실습 1. 주조 데이터 구조·분포 살펴보기")
# 실습 1. 주조 데이터 구조·분포 살펴보기

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 다이캐스팅 설비 데이터를 불러와 구조를 첫 진단

import pandas as pd

# 목표
# 주조 데이터를 불러와 크기·컬럼·자료형을 확인

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# read_csv로 데이터를 불러와 head로 앞부분 확인
print("==[ read_csv로 데이터를 불러와 head로 앞부분 확인 ]==\n")
df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
print(df.head(3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# shape와 columns로 크기와 컬럼 이름 확인
print("==[ shape와 columns로 크기와 컬럼 이름 확인 ]==\n")
print("--[ shape ]--\n")
print(df.shape)

print(f"\n{"~ "*10}\n")
print("--[ columns ]--\n")
print(df.columns.tolist())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# info로 자료형과 결측 여부 훑기
print("==[ info로 자료형과 결측 여부 훑기 ]==\n")
df.info()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
