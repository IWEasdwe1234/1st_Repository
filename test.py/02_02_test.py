# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)


import pandas as pd

tags = pd.read_csv("data/02-01_측정의_3요소_설비태그목록.csv")
df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
gaps = df["timestamp"].diff().value_counts()

cols = [
    "MTR01_VIB_RMS_H",
    "MTR01_CURRENT",
    "MTR01_TEMP",
    "HYD01_PRESS_IN",
    "FUR01_TEMP_Z1",
]

print(df[cols].agg(["min", "max", "mean"]).round(2))

print(ln2)
for c in cols:
    changes = df[c].diff().abs()
    min_change = changes[changes > 0].min()
    repeated = (changes == 0).sum()
    print(
        "\n태그 이름 :",
        c,
        "\n최소 차이 : ",
        round(min_change, 2),
        "\n반복횟수 :",
        repeated,
    )

print(ln1)
