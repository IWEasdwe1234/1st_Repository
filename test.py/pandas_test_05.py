# 실습 5. 경로·옵션 오류 고치기
print("\n실습 5. 경로·옵션 오류 고치기\n")

import pandas as pd

# 실습 과제 · 경로 오류 3개
# 경로 · 철자 · 확장자
# data/ 누락, 철자, .csv 누락 — 세 종류의 FileNotFoundError

# # data/ 누락
# df = pd.read_csv("12_metro_small.csv")
# # 결과 : [오류] FileNotFoundError

# # 철자
# df = pd.read_csv("data/metro_small.csv")
# # 결과 : [오류] FileNotFoundError

# df = pd.read_csv("data/12_metro_small")
# 결과 : [오류] FileNotFoundError

df = pd.read_csv("data/12_metro_small.csv")
print(df.shape)
# 결과 : [정상] (30, 7)
