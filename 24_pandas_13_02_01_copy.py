#

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df.info()

df_bad = df[df["품질등급"] == "불량"].copy()

# 만약 copy 없이 바로 df_bad의 모든 품질등급을 다른 내용으로 변경한다면? 경고가 발생할 수도 있음
df_bad["품질등급"] = "점검"

print(df_bad.head())
