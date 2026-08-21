# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
print(ln)

# 실습 3. 결측 비율 기준 컬럼 제거
print("실습 3. 결측 비율 기준 컬럼 제거")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 결측 비율이 높은 컬럼만 골라 제거

import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")
print(df.shape)  # (250, 22)

# 목표
# 결측 비율이 높은 컬럼만 골라 제거

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 단계
# 컬럼별 결측 비율을 계산
print("==[ 컬럼별 결측 비율을 계산 ]==\n")
df_rate = df.isna().sum() / len(df)
print(df_rate)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기
# -> 40% 이상 NaN으로 채워진 컬럼 목록
print("==[ 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기 ]==\n")
df_terminates = df_rate[df_rate > 0.4]
print(df_terminates)


print(f"\n{"~ "*10}\n")

# 최초 컬럼 이름들이 df_terminates의 index labels가 되었다.
print("--[ 최초 컬럼 이름들이 df_terminates의 index labels ]--\n")
list_terminates = df_terminates.index.tolist()
print(list_terminates)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 그 컬럼들을 drop으로 제거하고 크기 확인
# dropna에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
print("==[ 그 컬럼들을 drop으로 제거하고 크기 확인 ]==\n")
df_final = df.drop(columns=list_terminates)
df_final.info()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
