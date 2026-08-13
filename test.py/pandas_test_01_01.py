# 실습  1. head·tail로 디지털 신호 살펴보기
print("\n실습  1. head·tail로 디지털 신호 살펴보기\n")

import pandas as pd

# 실습 과제
# metro_digital_sample.csv
# 25열 300행, 결측 많음


# 12_metro_digital.csv
print("\n-- 12_metro_digital.csv --")
df = pd.read_csv("data/12_metro_digital.csv")

print("\n[shape 출력]")
print(df.shape)  # (120, 4)

# --------------------
print(f"\n{"-"*20}\n")

print("\n[head(4) 출력]")
print(df.head(4))

# --------------------
print(f"\n{"-"*20}\n")

print("\n[tail(3) 출력]")
print(df.tail(3))

# --------------------
print(f"\n{"-"*20}\n")

print("\n[head() 출력]")
print(df.head())

# ----------------------------------------
print(f"\n{"-"*40}\n")

# metro_digital_sample.csv
print("\n-- metro_digital_sample.csv --")
df = pd.read_csv("data/12_metro_small.csv")

print("\n[shape 출력]")
print(df.shape)  # (30, 7)

# --------------------
print(f"\n{"-"*20}\n")

print("\n[head(4) 출력]")
print(df.head(4))

# --------------------
print(f"\n{"-"*20}\n")

print("\n[tail(3) 출력]")
print(df.tail(3))

# --------------------
print(f"\n{"-"*20}\n")

print("\n[head() 출력]")
print(df.head())
