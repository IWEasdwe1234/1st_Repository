# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
ln1 = f"\n{"~ " * 10}\n"
print(ln)

print("실습 5. quantile로 Q1·Q2·Q3")
# 실습 5. quantile로 Q1·Q2·Q3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 실린더압력의 사분위수를 구하고 Q2와 중앙값 일치 확인

import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")


# 목표
# 사분위수를 구하고 Q2가 중앙값과 같은지 확인

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# 25% 지점 값을 quantile로 구해 Q1 확인
print("==[ 25% 지점 값을 quantile로 구해 Q1 확인 ]==\n")
print(df["실린더압력"].quantile(0.25))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 50% 지점 값이 중앙값과 같은지 확인
print("==[ 50% 지점 값이 중앙값과 같은지 확인 ]==\n")
print("-[ 50% 지점 ]-\n")
print(df["실린더압력"].quantile(0.5))
print(ln1)
print("-[ 중앙값 ]-\n")
print(df["실린더압력"].median())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# 75% 지점 값을 구해 가운데 절반 범위 파악
print("==[ 75% 지점 값을 구해 가운데 절반 범위 파악 ]==\n")
print(df["실린더압력"].quantile(0.75))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
