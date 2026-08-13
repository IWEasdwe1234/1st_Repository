# 실습 4. 열 이름·자료형 점검
print("\n실습 4. 열 이름·자료형 점검\n")

import pandas as pd

# 실습 과제
# 설비 센서 데이터 점검
# 12_metro_compressor.csv의 자료형 점검

df = pd.read_csv("data/12_metro_compressor.csv")

print("\n[.columns 출력]")
print(df.columns)

print("\n[.columns.tolist() 출력]")
print(df.columns.tolist())

print("\n[dtypes 출력]")
print(df.dtypes)
