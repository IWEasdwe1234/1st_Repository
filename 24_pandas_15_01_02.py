# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
l = f"\n{"~ " * 10}\n"


import pandas as pd

# -999와 999라는 값이 있다면 NaN으로 처리하기 -> na_values=[-999, 999]
df = pd.read_csv(
    "data/15_01_사출성형_공정.csv", encoding="utf-8", na_values=[-999, 999]
)
print(df.shape)  # (250, 22)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(l)

df.info()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(l)

print(df.describe())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(l)

print(df.isna().sum())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(l)

print(df.notna().sum())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(l)

# 각 컬럼별 NAN 갯수를 낸 Serise 대상으로 다시 합산을 시키면?
# -> 전체 NaN 갯수

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
