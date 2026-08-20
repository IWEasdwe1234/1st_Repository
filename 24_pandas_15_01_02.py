# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

import pandas as pd

# -999와 999라는 값이 있다면 NaN으로 처리하기 -> na_values=[-999, 999]
df = pd.read_csv(
    "data/15_01_사출성형_공정.csv", encoding="utf-8", na_values=[-999, 999]
)
print(df.shape)  # (250, 22)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 10}\n")

df.info()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 10}\n")

print(df.describe())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
