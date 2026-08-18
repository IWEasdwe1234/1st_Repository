# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 2. 비율과 불균형 데이터")
# 실습 2. 비율과 불균형 데이터

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")


import pandas as pd

df_qc = pd.read_csv("data/14_hydraulic_qc.csv")
df_qc.info()
print(df_qc.head(3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 목표
# 합격·불합격 빈도와 비율을 구해 불균형 데이터 확인

# 단계
# 공정 데이터의 판정 열에 value_counts로 합격·불합격 개수 세기
print("== 합격·불합격 개수 세기 ==\n")
print(df_qc["검사결과"].value_counts())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

# normalize 옵션으로 각 값의 비율을 소수로 확인
print("== 각 값의 비율을 소수로 확인 ==\n")
print(df_qc["검사결과"].value_counts(normalize=True))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

# round로 비율을 소수점 셋째 자리까지 정리
print("== 비율을 소수점 셋째 자리까지 정리 ==\n")
print(df_qc["검사결과"].value_counts(normalize=True).round(3))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
