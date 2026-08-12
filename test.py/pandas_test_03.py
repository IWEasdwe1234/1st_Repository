# 실습 3. 한글·구분자 깨짐 옵션 다루기
print("\n실습 3. 한글·구분자 깨짐 옵션 다루기\n")

# 실습 과제
# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd

# sep=";"없음
print('sep=";"없음')
df = pd.read_csv("data/12_metro_compressor_semicolon.csv")
print(df.shape)  # (200, 1)

# sep=";"있음
print('\nsep=";"있음')
df = pd.read_csv("data/12_metro_compressor_semicolon.csv", sep=";")
print(df.shape)  # (200, 7)
