# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 7. 빈도와 그룹 집계 종합")
# 실습 7. 빈도와 그룹 집계 종합

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 빈도 집계와 그룹 집계를 한 흐름으로 연결

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")
df.info()
print(df.head(4))

# 목표
# 빈도 집계와 그룹 집계를 한 흐름으로 연결해 분석

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")


# 단계
# value_counts로 설비 구성과 정상·고장 비율 파악
# 밸브상태별로 비율 확인 - 일단 각 상태별로 몇 건이 있는지 확인
# group-size와 다르게 여기는 counts라서 결측(null값) 무시
print(df["밸브상태"].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19

# ~ ~ ~ ~ ~
print(f"\n{"~ " * 5}\n")

print(df["밸브상태"].value_counts(normalize=True).round(3))
# 밸브상태
# 정상    0.508
# 지연    0.167
# 경미    0.167
# 심각    0.158

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 10}\n")

# 고장 행만 걸러 라인별 고장 건수 집계
# 다음 세가지 방법이 있다. 차이점은 잘 파악해주세요!
df_bad = df[df["result"] == "고장"]
print(len(df_bad))  # 53 -> 문제에 가장 부합!

# ~ ~ ~ ~ ~
print(f"\n{"~ " * 5}\n")

print(df.groupby("result").size())
# result
# 고장    53
# 정상    67

# ~ ~ ~ ~ ~
print(f"\n{"~ " * 5}\n")

print(df["result"].value_counts())
# result
# 정상    67
# 고장    53

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 10}\n")

# groupby로 설비별 온도·진동 평균까지 비교
print(df.groupby("냉각기상태")["온도"].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89

# ~ ~ ~ ~ ~
print(f"\n{"~ " * 5}\n")

print(df.groupby("냉각기상태")["진동"].mean().round(2))
# 냉각기상태
# 고장    0.69
# 저하    0.61
# 정상    0.55

# ~ ~ ~ ~ ~
print(f"\n{"~ " * 5}\n")

# 각각처리하지 말고 한번에!
print(df.groupby("냉각기상태")[["온도", "진동"]].mean().round(2))
#           온도    진동
# 냉각기상태
# 고장     54.67  0.69
# 저하     45.46  0.61
# 정상     35.89  0.55

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
