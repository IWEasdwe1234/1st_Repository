# 실습 5. loc·iloc로 행·열 동시 선택하기
print("실습 5. loc·iloc로 행·열 동시 선택하기")

import pandas as pd

# 목표
# 행과 열을 동시에 지정해 원하는 부분만 추출

# data/13_diecasting_small.csv 사용
df = pd.read_csv("data/13_diecasting_small.csv")


# 단계
# loc로 행 범위와 열 이름을 함께 지정
df_sub = df.loc[0:4, ["품질등급", "형체력"]]
print("\ndf_sub.shape 출력\n")
print(df_sub.shape)  # (5, 2)

# ----------------------------------------
print(f"\n{"-" * 40}\n")

# 다른 행 범위에서 세 열 선택
df_sub2 = df.loc[10:14, ["형체력", "실린더압력", "주조압력"]]
print("df_sub2.shape 출력\n")
print(df_sub2.shape)  # (5, 3)

# ----------------------------------------
print(f"\n{"-" * 40}\n")

# # iloc 음수 인덱스로 마지막 행 선택
print("len(df.iloc[-3:]) 출력\n")
print(len(df.iloc[-3:]))  # 3
