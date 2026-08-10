# == 실습 4. 배열 구조 확인하기 ==
print("== 실습 4. 배열 구조 확인하기 ==")

import numpy as np

# 설비별 측정값을 담은 이차원 배열 준비
a = np.array([[24, 44], [16, 4]])

# ndim으로 차원, shape으로 형태, size로 전체 개수 확인
# 세 속성값 출력
print(f"ndim : {a.ndim}")  # 2
print(f"shape : {a.shape}")  # (2, 2)
print(f"size : {a.size}")  # 4
