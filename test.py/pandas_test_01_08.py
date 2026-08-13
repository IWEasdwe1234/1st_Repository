# 실습 8. 압축기와 디지털 신호 구조 비교
print("\n실습 8. 압축기와 디지털 신호 구조 비교\n")

import pandas as pd

# 안내
# 두 데이터를 모두 다룬다 (강사 제공)
# 각 데이터를 다른 변수에 담아 비교 — df_metro_compressor, df_metro_digital

# "data/12_metro_compressor.csv"
# "data/12_metro_digital.csv"
# shape, info, describe

df_compressor = pd.read_csv("data/12_metro_compressor.csv")
print("df_compressor.shape 출력\n")
print(df_compressor.shape)  # (200, 7)

print(f"\n{"-"*20}\n")

df_digital = pd.read_csv("data/12_metro_digital.csv")
print("df_digital.shape 출력\n")
print(df_digital.shape)  # (120, 4)

# ----------------------------------------
print(f"\n{"-"*40}\n")

df_compressor = pd.read_csv("data/12_metro_compressor.csv")
print("df_compressor.shape 출력\n")
print(df_compressor.shape)  # (200, 7)

print(f"\n{"-"*20}\n")

df_digital = pd.read_csv("data/12_metro_digital.csv")
print("df_digital.shape 출력\n")
print(df_digital.shape)  # (120, 4)
