# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 1. value_counts로 빈도 세기")
# 실습 1. value_counts로 빈도 세기

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")


import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")
df.info()
print(df.head(3))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
# 목표
# 한 열의 값별 개수를 세어 데이터 구성 파악

# 단계
# 설비 데이터를 불러와 앞부분과 구조 확인
print("== 구조 확인 ==\n")
print(df["result"].value_counts())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

# 설비 열에 value_counts를 붙여 값별 개수 세기
print("== 값별 개수 세기 ==\n")
equipment_count = df["밸브상태"].value_counts()
print(equipment_count)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

# 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print("== 가장 많은 값 확인 ==\n")
shift_count = df["운전부하"].value_counts()
print(shift_count)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
