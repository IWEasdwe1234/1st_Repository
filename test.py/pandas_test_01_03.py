# 실습 3. 구조 파악 3종 도구
print("\n실습 3. 구조 파악 3종 도구\n")

import pandas as pd

# 실습 과제
# metro_digital_sample.csv
# 25열, 결측 많음

df = pd.read_csv("data/12_metro_digital.csv")
print("\n[shape 출력]")
print(df.shape)  # (120, 4)

# ----------------------------------------
print(f"\n{"-"*40}\n")

print("\n[columns 출력]")
print(df.columns)

# ----------------------------------------
print(f"\n{"-"*40}\n")

print("\n[columns.tolist() 출력]")
print(df.columns.tolist())

# ----------------------------------------
print(f"\n{"-"*40}\n")

print("\n[dtypes 출력]")
print(df.dtypes)
