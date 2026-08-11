# 실습 3. 센서값 정규화하기

# 목표
# 회전수 배열을 0과 1 사이 값으로 정규화

import numpy as np

# 단계
# 회전수 측정 배열 준비
rpm = np.array([1551, 1408, 1498, 1433, 1425, 2861])


# 최솟값과 최댓값을 min, max로 확인
print(rpm.min())  # 1408
print(rpm.max())  # 2861

# 정규화 공식을 브로드캐스팅으로 적용해 변환
# 정규화 공식
# 정규화된x = (비교대상 - 최솟값) / (최댓값 - 최솟값)
x = (rpm - rpm.min()) / (rpm.max() - rpm.min())
print(x)
print(np.round(x, 2))
