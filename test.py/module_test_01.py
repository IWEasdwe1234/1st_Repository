# ========================================
print("\n" + "=" * 40 + "\n")

print("실습 1.import 세 방식으로 모듈 가져오기")

# 목표
# import·from import·as 세 방식으로 같은 기능을 가져와 써 보기

# 단계
# ① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용

# ② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용

# ③ import 모듈 as 별명 으로 별명.기능() 으로 사용

# ④ 세 방식의 출력이 같은지 확인


# ========================================
print("\n" + "=" * 40 + "\n")

# ① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용
print("① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용\n")

import math

math.sqrt(16)

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용
print("② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용\n")

from math import sqrt

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ③ import 모듈 as 별명 으로 별명.기능() 으로 사용
print("③ import 모듈 as 별명 으로 별명.기능() 으로 사용\n")

import math as mt

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

print("④ 세 방식의 출력이 같은지 확인\n")

# ①
import math

print("①", math.sqrt(16))  # 4.0

# ②
from math import sqrt

print("②", sqrt(16))  # 4.0

# ③
import math as mt

print("③", mt.sqrt(16))  # 4.0
