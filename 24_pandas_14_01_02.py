# pd. cut 구간 빈도 코드

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")
df.info()
print(df.head(3))

print(df["온도"].value_counts())
# 위와 같이 범위 없이 개별 경우의 수를 따지면 62가지나 되버린다
# 그래서 범위를 설정해 경우의 수를 줄여보기 -> 범주화


band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"])
print(band.value_counts())
# 온도
# 낮음    41
# 보통    40
# 높음    39
