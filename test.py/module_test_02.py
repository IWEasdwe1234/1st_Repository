# ========================================
print("\n" + "=" * 40 + "\n")

print("실습 2.표준 라이브러리로 센서값 만들기")
# 실습 2.표준 라이브러리로 센서값 만들기

# 목표
# random·math 모듈로 무작위 센서값을 만들고 가공하기

# 단계
#   ① random 모듈을 import

#   ② randint로 무작위 센서값을 만들어 출력

#   ③ math 모듈로 그 값을 가공(제곱근)

#   ④ 다시 실행하면 값이 달라지는지 확인

# ========================================
print("\n" + "=" * 40 + "\n")

# ① random 모듈을 import
print("① random 모듈을 import\n")

import random

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ② randint로 무작위 센서값을 만들어 출력
print("② randint로 무작위 센서값을 만들어 출력\n")

print(random.randint(1, 50))

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ③ math 모듈로 그 값을 가공(제곱근)
print("③ math 모듈로 그 값을 가공(제곱근)\n")

import math

result = random.randint(1, 50)
print(f"값: {result}\n제곱근: {math.sqrt(result)}")

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ④ 다시 실행하면 값이 달라지는지 확인
print("④ 다시 실행하면 값이 달라지는지 확인\n")

result = random.randint(1, 50)
print(f"값: {result}\n제곱근: {math.sqrt(result)}")
