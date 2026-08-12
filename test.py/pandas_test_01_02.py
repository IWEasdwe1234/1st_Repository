# 실습 2. head·tail 행 개수 조절
print("\n실습 2. head·tail 행 개수 조절\n")

import pandas as pd

# 실습 과제
# 설비 센서 데이터
# 12_metro_compressor.csv로 연습

df = pd.read_csv("data/12_metro_compressor.csv")

print("\n[head(1) 출력]")
print(df.head(1))

print("\n[head(10) 출력]")
print(df.head(10))

print("\n[tail(7) 출력]")
print(df.tail(7))

print("\n[head(500) 출력]")
print(df.head(500))
