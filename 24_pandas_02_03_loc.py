# 복수열 선택 선택

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()  # <class 'pandas.DataFrame'>

# ----------------------------------------
print(f"\n{"-" * 40}\n")

df.loc[0].info()  # Series <class 'pandas.Series'>

# ----------------------------------------
print(f"\n{"-" * 40}\n")

df.loc[0:2].info()  # DataFrame <class 'pandas.DataFrame'>
