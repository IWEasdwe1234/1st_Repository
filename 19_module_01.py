# ========================================
print("\n" + "=" * 40 + "\n")

print("모듈과 import\n")

# 수학 관련 모듈을 불러옵니다
import math

result = math.sqrt(16)
print(result)  # 4.0


# 수학 관련 모듈에서 sqrt 기능만 불러옵니다
from math import sqrt

# ========================================
print("\n" + "=" * 40 + "\n")

# 이젠 sqrt만 불러도 됩니다
result = sqrt(16)
print(result)  # 4.0


# ========================================
print("\n" + "=" * 40 + "\n")

# math라는 모듈 이름 다 쓰기 귀찮아서 줄여봅시다
import math as mt

# 별칭으로 가져온 모듈 이름을 언급해봅시다
result = mt.sqrt(16)
print(result)  # 4.0


# ========================================
print("\n" + "=" * 40 + "\n")

# datetime 모듈을 가져옵니다
import datetime as dt

# datetime의 now()는 현재의 지역 날짜와 시간을 반환합니다.
now = dt.datetime.now()
print(now)  # 2026-08-05 11:23:14.000773
print(type(now))  # <class 'datetime.datetime'>

# ========================================
print("\n" + "=" * 40 + "\n")

print("표준 라이브러리\n")
