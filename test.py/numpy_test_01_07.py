# == 실습 7. 파일 데이터로 기초 통계 구하기 ==
print("== 실습 7. 파일 데이터로 기초 통계 구하기 ==")

# 목표
# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산

import numpy as np

# 단계
# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf -8"
)


# 불러온 배열의 평균과 표준편차 계산
print(round(rpm.mean(), 1))
print(round(rpm.std(), 1))


# 최솟값과 최댓값으로 값의 범위 확인
print(rpm.min(), rpm.max())
print(rpm.max() - rpm.min())
