# 1차원 인덱싱 - 번호로 값 꺼내기

# 배열의 인덱스 번호는 파이썬 리스트처럼 0부터 시작

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp)  # [70 72 71 95 73]

# 첫번째 내용만 콕찝어 보여주기
print(temp[0])  # 70

print(temp[-1])  # 73

# ====================
print(f"\n{"="*20}\n")

# 1차원 슬라이싱

# 시작 : 끝으로 구간 잘라내기 (끝 번호는 제외)

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp)  # 70 72 71 95 73

# 0번째부터 시작하는 배열 내용에서
# 1번째인 항목부터 4번째 항목 아전의 3번까지를 슬라이스로 뽑아낸다
print(temp[1:4])  # [72 71 95]

print(temp[::2])  # [70 71 73]

# ====================
print(f"\n{"="*20}\n")

# 2차원 인덱스

import numpy as np

data = np.array([[70, 2.1], [72, 2.3]])

# 기존 리스트처럼 특정 위치 지정해 콕 찝어오기
print(data[0][1])


# 대부분의 numpy의 배열은 수학공식 같은 식으로 위치를 지정한다
# 0행(row) 1열(column)
print(data[0, 1])

# ====================
print(f"\n{"="*20}\n")

# 2차원 슬라이싱 - 행/열 선택
print(f"2차원 슬라이싱 - 행/열 선택\n")
# 행 전체, 열 전체, 일부 구간 잘라내기 - 콜론이 전부를 의미

import numpy as np

data = np.array([[70, 2.1], [72, 2.3]])
print(data)

# ----------
print(f"\n{"-"*10}\n")

# 0번째 줄(행, row) 전체
print(f"0번째 줄 전체\n")
print(data[0])

# 콜론(:)은 해당 배열에서 갖을 수 있는 모든 모든 경우를 의미
# 이 배열에서 row부분에 콜론(:)d이 있다면
# 0과 1을 의미한다
# 결과적으로 특정 열(컬럼, column)만 쭉 뽑아오기 가능
print(data[:, 0])

# ====================
print(f"\n{"="*20}\n")

print(f"배열의 산술 연산\n")
# 배열의 산술 연산
# 두 배열을 같은 위치끼리 한 번에 계산

import numpy as np

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)  # [11 22 33]
print(x * 2)  # [2 4 6]
print(y * 2)  # [20 40 60]
print(x * y)  # [10 40 90]

# ====================
print(f"\n{"="*20}\n")

print(f"스칼라 연산\n")
# 배열 안의 섭씨 온도들을 화씨 온도로 바꿔 출력하기
celsius = np.array([20.0, 25.0, 30.0])
# 화씨온도 = 섭씨온도 * 1.8 + 32)
f = celsius * 1.8 + 32
print(f)  # [68. 77. 86.]

# 스칼라 연산은 위 예제처럼
# 배열 전체에 항목마다 계산시켜 다시 새로운 배열 만들기

# ====================
print(f"\n{"="*20}\n")

print(f"브로드캐스팅\n")
# 한 줄짜리 기준값이 모든 행에 퍼져서 계산

table = np.array([[72, 2.3], [95, 6.8]])

base = np.array([70, 2.0])

# table의 각 행에서 기준값(base)을 빼기
print(table - base)

# ====================
print(f"\n{"="*20}\n")

print(f"비교 연산과 불리언 배열\n")

v = np.array([70, 95, 71, 88, 73])
print(v > 85)  # [False  True False  True False]

# ----------
print(f"\n{"-"*10}\n")

# Boolean indexing
# 불리언 배열로 조건에 맞는 값만 골라내기
print(v[v > 85])  # [95 88]

# ----------
print(f"\n{"-"*10}\n")

# np.where 조건 처리
# 조건에 따라 값을 둘 중 하나로 바꾸기
# - 조건/참/거짓 ... 세 가지 인자
# 조건이 참이면 1(위험)
# 조건이 0(정상)

print(np.where(v > 85, 1, 0))
# [0 1 0 1 0]

# ----------
print(f"\n{"-"*10}\n")

# 다중 조건 결합
print(v)  # [70 95 71 88 73]
v_step1 = v[v > 70]
print(v_step1)  # [95 71 88 73]
v_step2 = v_step1[v_step1 < 90]
print(v_step2)  # [71 88 73]

v_mixed = v[(v > 70) & (v < 90)]
print(v_mixed)  # [71 88 73]

# 참고, 조건 대신 True를 직접 준다면?
print(v[True])  # [[70 95 71 88 73]]
