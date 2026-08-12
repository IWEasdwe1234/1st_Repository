# 실습 1. CSV불러오기 워밍업
print("\n실습 1. CSV불러오기 워밍업\n")

import pandas as pd

# 실습 과제
# 설비 3대 측정값
# 열: 측정시각, 오일온도, 모터전류

df = pd.read_csv(
    "data/12_metro_small.csv", usecols=["측정시각", "오일온도", "모터전류"]
)
print(df)
