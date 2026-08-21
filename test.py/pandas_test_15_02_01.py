# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
print(ln)

print("실습 1. dropna로 행·열 삭제")
# 실습 1. dropna로 행·열 삭제

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 결측 있는 행과 열을 삭제하고 크기 변화 확인

import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")

# 목표
# 결측 있는 행과 열을 삭제하고 크기 변화 확인

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# 원본 크기를 shape로 확인
print("==[ shape로 확인 ]==\n")
print(df.shape)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# dropna로 결측 있는 행을 모두 삭제
print("==[ dropna로 결측 있는 행을 모두 삭제 ]==\n")
print(df.dropna().shape)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 방향을 열로 바꿔 결측 있는 열을 삭제
print("==[ 방향을 열로 바꿔 결측 있는 열을 삭제 ]==\n")
print(df.dropna(axis=1).shape)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
