# 1차원 인덱싱 - 번호로 값 꺼내기

# 배열의 인덱스 번호는 파이썬 리스트처럼 0부터 시작

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp)  # [70 72 71 95 73]

# 첫번째 내용만 콕찝어 보여주기
print(temp[0])  # 70

print(temp[-1])  # 73


# 1차원 슬라이싱

# 시작 : 끝으로 구간 잘라내기 (끝 번호는 제외)

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp)  # 70 72 71 95 73

# 0번째부터 시작하는 배열 내용에서
# 1번째인 항목부터 4번째 항목 아전의 3번까지를 슬라이스로 뽑아낸다
print(temp[1:4])  # [72 71 95]

print(temp[::2])  # [70 71 73]


# 2차원 인덱스

import numpy as np

data = np.array([[70, 2.1], [72, 2.3]])

# 기존 리스트처럼 특정 위치 지정해 콕 찝어오기
print(data[0][1])


# 대부분의 numpy의 배열은 수학공식 같은 식으로 위치를 지정한다
# 0행(row) 1열(column)
print(data[0, 1])
