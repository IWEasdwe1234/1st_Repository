# == 실습 6. 센서별 기초 통계 구하기 ==
print("== 실습 6. 센서별 기초 통계 구하기 ==")

# 목표
# 표 모양 데이터에서 센서별(열별) 통계 계산

import numpy as np

# 단계
# 여러 설비의 회전수·토크 이차원 배열 준비
data = np.array([[1551, 42.8], [1408, 46.3], [1498, 49.4], [2861, 4.6]])


# axis를 열 방향으로 지정해 센서별 평균 계산
print(data.mean(axis=0))
print(data.mean(axis=1))


# 센서별 표준편차 계산
print(data.std(axis=0))
print(np.round(data.std(axis=0), 2))
