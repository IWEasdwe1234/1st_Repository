# 2차원

import numpy as np

# 기존 파이썬 리스트로 2차원을 표현
dim_2_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 3, 6],
]

print(dim_2_list[0][0])  # 1
print(dim_2_list[1][1])  # 7

# numpy에서 배열이라면?
dim_2_array = np.array(dim_2_list)
print(dim_2_array)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [ 2  4  6  8 10]
#  [ 3  6  9  3  6]]

print(dim_2_array[0][0])  # 1
print(dim_2_array[1][1])  # 7

# numpy 배열에서는 다음 방식으로
# 2차원 배열 내용을 가리키는게 일반적
print(dim_2_array[0, 0])  # 1
print(dim_2_array[1, 1])  # 7

# ====================
print(f"\n{"="*20}\n")

# 이 배열은 몇 차원인지 알아보기
print(dim_2_array.ndim)  # 2

# 이 배열의 형태 알아보기 (몇 행, 몇 컬럼)
print(dim_2_array.shape)  # (4, 5)

# 배열의 크기 알아보기 (보통 행 * 컬럼)
print(dim_2_array.size)  # 20 = 4 * 5

# 배열 안의 내용물이 어떤 타입인지 알아보기
print(dim_2_array.dtype)  # int64


# ====================
print(f"\n{"="*20}\n")

# 형변환(astype)
# 예를들어 아래의 float들로 가득한 배열이 있다면
convertable = np.array([3.14, 6.7, 1.23])
print(convertable.dtype)  # float64

# int들로 가득한 배열로 알아서 바꿔준다
converted = convertable.astype(int)
print(converted)  # [3 6 1]
print(converted.dtype)  # int64
