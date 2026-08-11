# == 실습 8. 필터링과 통계 결합하기 ==
print("== 실습 8. 필터링과 통계 결합하기 ==")

# 목표
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산

import numpy as np

# 단계
# 토크 배열 준비
torque = np.array([42.8, 46.3, 49.4, 65.7, 41.9, 60.7, 40.2, 4.6])


# 불리언 인덱싱으로 기준을 넘는 값만 추출
high = torque[torque > 50]
print(high)


# 추출한 값들의 평균과 개수 계산
print(round(high.mean(), 1))
print(high.size)
