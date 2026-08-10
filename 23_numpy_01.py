import numpy as np

# 파이썬의 리스트로부터 NumPy 배열 만들기
temp = np.array([70.5, 69.8, 73.7])

print(temp)  # [70.5 69.8 73.7] 항목 사이에 콤마 없음 유의

# 배열의 항목들마다 +5씩 더하려면?
# 리스트였다면 for문으로 돌려서 항목마다 직접 처리해줬어야 함
# NumP라면 간단하게
print(temp + 5)  # [75.5 74.8 78.7]

# 소숫점 이하가 없는 숫자 타입들로 가득찬 배열
print(np.array([1, 2, 3, 4, 5]))  # [1 2 3 4 5]

# 소숫점 이하가 있는 숫자 타입들로 가득찬 배열
print(np.array([3.14, 6.7, 7.67]))  # [3.14 6.7  7.67]

# 소숫점 이하가 있는것 없는것이 섞여있다면?
# 모두 소수점 이하가 있는 것으로 배열 생성
print(np.array([1, 3, 5, 3.14, 6.7, 4]))
# [1.   3.   5.   3.14 6.7  4.  ]


# == np.arange ==
print("\n== np.arange ==\n")

import numpy as np

# 0부터 4까지 생성
under_five = np.arange(5)
print(under_five)  # [0 1 2 3 4]

# 0부터 8까지 2간격 (8보다 큰 숫자가 만들어지면 덧붙이지 않고 끝)
gab_two = np.arange(0, 10, 2)
print(gab_two)  # [0 2 4 6 8]


# == np.linspace ==
print("\n== np.linspace ==\n")

import numpy as np

# linspace
# 개수 중심 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 정확히 나눕니다
# 간격은 알아서 계산하도록 함

# 0부터 1까지 5개로 균등 분할
div_five = np.linspace(0, 1, 5)
print(div_five)  # [0.   0.25 0.5  0.75 1.  ]


# == zeros, ones, full 초기화 배열 ==
print("\n== zeros, ones, full 초기화 배열 ==\n")

import numpy as np

# 0으로 채우기
block_zeros = np.zeros(5)
print(block_zeros)  # [0. 0. 0. 0. 0.]

# 7으로 채우기
block_seven = np.full(4, 7)
print(block_seven)  # [7 7 7 7]

# 명시적으로 7.0처럼 float값을 지정해줘야
# float 타입 값으로 채워지는 배열이 만들어진다.
block_seven = np.full(4, 7.0)
print(block_seven)  # [7. 7. 7. 7.]
