# 복수열 선택 선택

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

print("\n")

# 데이터 프레임에서 컬럼 한개를도려내보면 시리즈(1차원)가 된다
df["형체력"].info()  # Series
df[["형체력", "실린더압력"]].info()  # DataFrame
