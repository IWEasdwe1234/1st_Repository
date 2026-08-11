# == 실습 9. NumPy 기초 종합 분석 ==
print("== 실습 9. NumPy 기초 종합 분석 ==")

# 목표
# 데이터 불러오기, 구조 확인, 필터링, 통계를 하나의 흐름으로 수행

import numpy as np

# 단계
# np.loadtxt로 회전수와 토크 두 열을 불러오기
data = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=(4, 5), encoding="utf -8"
)


# shape과 dtype으로 구조 확인
print(data.shape, data.dtype)


# 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rpm = data[:, 0]
print(rpm)
anomaly = rpm[rpm < 1000]
print(anomaly)
print(anomaly.size, round(anomaly.mean(), 1))
