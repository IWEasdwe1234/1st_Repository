# == 실습 3. 측정 시간축 배열 만들기 ==
print("== 실습 3. 측정 시간축 배열 만들기 ==")

import numpy as np

# 시작값·끝값·간격을 정해 np.arange로 시점 배열 생성
num = np.arange(0, 30, 10)

# 간격을 바꿔가며 시점 개수 변화 관찰
num = np.arange(0, 30, 6)
# 시점 개수 : 3개 → 5개

# 시간축 배열 출력
print(num)  # [ 0  6 12 18 24]
