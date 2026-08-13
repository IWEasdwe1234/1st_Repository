# 실습 4. 열 이름·자료형 점검
print("\n실습 4. 열 이름·자료형 점검\n")

import pandas as pd

# 실습 과제
# 설비 센서 데이터 점검
# 12_metro_compressor.csv의 자료형 점검

df = pd.read_csv("data/12_metro_compressor.csv")

print("[.columns 출력]\n")
print(df.columns)

# ----------------------------------------
print(f"\n{"-"*40}\n")

print("[.columns.tolist() 출력]\n")
print(df.columns.tolist())

# ----------------------------------------
print(f"\n{"-"*40}\n")

print("[dtypes 출력]\n")
print(df.dtypes)
