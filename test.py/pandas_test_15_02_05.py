# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
print(ln)

# 실습 5. fillna 평균·중앙값 대체
print("실습 5. fillna 평균·중앙값 대체")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 결측을 평균과 중앙값으로 채우고 차이 이해

import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")


# 목표
# 결측을 평균과 중앙값으로 채우고 차이 이해

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# 대상 컬럼의 평균과 중앙값을 각각 구해 비교
print("==[ 대상 컬럼의 평균과 중앙값을 각각 구해 비교 ]==\n")
print(df["최대사출압"].isna().sum())  # 60개 NaN 확인


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# fillna로 평균을 채운 결과 만들기
print("==[ fillna로 평균을 채운 결과 만들기 ]==\n")
mean = df["최대사출압"].mean()
print(f"최대사출압의 평균 : {mean}")  # 1241.6723684210526

s_fillmean = df["최대사출압"].fillna(mean)
print(s_fillmean)
df["최대사출압"] = s_fillmean
print(df["최대사출압"].isna().sum())  # 최대사출압 컬럼의 0개

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
print("==[ fillna로 중앙값을 채운 결과 만들기(이상치에 강함) ]==\n")
median = df["최대사출압"].median()
print(f"최대사출압의 중앙값 : {median}")  # 1240.84

print(f"\n{"~ "*10}\n")
s_fillmean = df["최대사출압"].fillna(median)
print(s_fillmean)

print(f"\n{"~ "*10}\n")
df["최대사출압"] = s_fillmean
print(df["최대사출압"].isna().sum())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
