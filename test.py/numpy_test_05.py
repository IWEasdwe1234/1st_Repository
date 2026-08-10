# == 실습 5. 자료형 확인과 변환하기 ==
print("== 실습 5. 자료형 확인과 변환하기 ==")

import numpy as np

# 소수점이 있는 측정값 배열 준비
a = np.array([1.2, 3.4, 5.6])


# dtype으로 현재 자료형 확인
print(a.dtype)  # float64


# astype으로 정수형으로 변환한 새 배열 출력
int_a = a.astype(int)
print(int_a)  # [1 3 5]
