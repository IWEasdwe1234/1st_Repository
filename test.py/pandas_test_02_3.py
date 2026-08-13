# 실습 3. 공정 센서 열 골라내기 ==
print("실습 3. 공정 센서 열 골라내기 ==")

import pandas as pd

# 목표
# 주조 로그 공정 데이터에서 원하는 센서 열 선택

# 단계
# 주조 로그 파일 불러오기
# data/13_diecasting_shot.csv 파일 열기
df = pd.read_csv("data/13_diecasting_shot.csv")

# 한 센서 열을 Series로 선택
# '형체력' 선택
print(df["형체력"])

print(f"\n{"-"*40}\n")

# 여러 feature 열을 DataFrame으로 선택해 형태 확인
# df[['형체력', '실린더압력', '주조압력']].shape 출력
print(df[["형체력", "실린더압력", "주조압력"]].shape)
