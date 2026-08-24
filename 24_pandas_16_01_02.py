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
print(mask.sum())
print(df[mask].shape)
print(df[~mask].shape)  # ~은 NOT이라는 여집합을 의미 -> 정상범위

print(ln2)
print(round(mask.mean() * 100, 1))

print(ln2)
# 정상범위는 다음의 마스크를 사용해도 됨
mask_ok = (df["사이클타임"] >= lower) & (df["사이클타임"] <= upper)
print(df[mask_ok].shape)
