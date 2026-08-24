# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)

import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 사이클타임 컬럼의 IQR 활용
q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)
print(f"Q1 : {q1}\nQ3 : {q3}")

iqr = q3 - q1
print(f"IQR : {iqr}")

print(ln1)
# 상한선과 하한선은 IQR의 1.5배를 적용한다
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"하한선 : {lower}\n상한선 : {upper}")

print(ln1)

# 상한선과 하한선을 이용해서 필터링할 조건을 만들 수 있다.
# 상한선 ~ 하한선 안쪽 : 정상범위로 판단
# 상한선과 하한선 바깥 : 이상하다고 판단
mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

df_clean = df[~mask]
print(len(df), len(df_clean))
print(df_clean["사이클타임"].mean())

# 경계값으로 보정하기
# clip(lower, upper) 보정 :
df["사이클타임_clipped"] = df["사이클타임"].clip(lower=lower, upper=upper)
print(df["사이클타임_clipped"].agg(["min", "max", "mean"]))

print(ln2 + "\n[결측치로 바꿔 채우기]\n")
# 결측치로 바꿔 채우기
s_masked = df["사이클타임"].mask(mask)
s_masked.info()

print(ln2)
print(s_masked.head())
print(s_masked.isna().sum())
print(ln2 + "\n[중앙값을 계산할때 NaN은 제외]\n")
s_fixed = s_masked.fillna(s_masked.median())  # 중앙값을 계산할때 NaN은 제외한다
print(s_fixed.mean())

print(ln1)
