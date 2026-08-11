# == 실습 5. 조건별 개수와 비율 세기 ==
print("== 실습 5. 조건별 개수와 비율 세기 ==")

# 목표
# 조건을 만족하는 값의 개수와 전체 대비 비율 계산

import numpy as np

# 단계
# 토크 배열 준비
torque = np.array([42.8, 46.3, 49.4, 4.6, 41.9, 65.7, 40.2, 60.7])


# 비교 조건으로 참·거짓 불리언 배열 생성
high = torque > 50
print(high)
print(torque[torque > 50])


# 불리언 배열의 합으로 개수, 평균으로 비율 계산
print(high.sum())
print(round(high.mean(), 2))
