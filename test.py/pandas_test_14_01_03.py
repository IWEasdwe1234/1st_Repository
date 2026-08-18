# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 3. 구간으로 묶어 세기")
# 실습 3. 구간으로 묶어 세기

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# pd.cut으로 수치형 값을 구간으로 묶어 빈도 세기


import pandas as pd

# 목표
# 수치형 센서 값을 구간으로 나눠 분포 확인


# 단계
# 진동 열의 최솟값과 최댓값으로 값의 범위 확인
df = pd.read_csv("data/14_hydraulic.csv")
df.info()
print(df.head(3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("== 최댓값 ==\n")
print(df["진동"].max())  # 0.779

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 10}\n")

print("== 최솟값 ==\n")
print(df["진동"].min())  # 0.53

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기
print("== 경계와 이름표를 정해 세 구간으로 묶기 ==\n")
band = pd.cut(df["진동"], bins=[0.0, 0.6, 0.7, 10.0])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 묶은 구간에 value_counts로 구간별 빈도 세기
print("== 구간별 빈도 세기 ==\n")
print(band.value_counts())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 10}\n")

print("== .round(3) 추가 ==\n")
print(band.value_counts(normalize=True).round(3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
