# 실습 2. 설비 센서 csv 불러오기
print("\n실습 2. 설비 센서 csv 불러오기\n")

import pandas as pd

# 실습 과제
# 12_metro_compressor.csv
# 200행 7열 — 인덱스 3번 행 오일온도가 NaN

df = pd.read_csv("data/12_metro_compressor.csv", usecols=["오일온도"])
print(df.head(5))
