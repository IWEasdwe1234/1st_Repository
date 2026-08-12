# 실습 4. 필요한 열만 골라 불러오기
print("\n실습 4. 필요한 열만 골라 불러오기\n")

# 실습 과제
# 센서 3개만 골라 불러오기
# usecols=[...]

import pandas as pd

df = pd.read_csv(
    "data/12_metro_compressor.csv", usecols=["압축압력", "저장압력", "가동상태"]
)
print(df.head(3))
