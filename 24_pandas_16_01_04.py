# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)

import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# print(df.duplicated()): 데이터프레임 내에서 완벽하게 내용이 겹쳐서 존재하는 중복 행 여부를 불리언 시리즈로 반환합니다.
print(df.duplicated())  # True/ False의 Boolean Serise

print(ln2)
print(df[df.duplicated()])  # "완전" 중복된 row들만 df로 추려내기

print(ln1)
# 중복 개수 확인하기
print(df.duplicated().sum())  # 2 row들이 중복으로 더 존재함 (먼저 확인 row 제외)
print(
    len(df)
)  # 202 : 전체가 202개 row로 2개 중복 빼면 순수하게 200개가 한 줄씩 안겹치고 존재


print(ln1)
print(df.duplicated(keep=False).sum())  # 4개의 중복 row들을 모두 제거 대상으로

print(ln1)
# 중복제거
print(df.duplicated().reset_index(drop=True))  # 4개의 중복 row들을 모두 제거 대상으로

# 부분중복 사례 제거 : "샷", "실린더입력", "주조압력" 컬럼만 중복되면 제거 대상!
print(df.duplicated(subset=["샷", "실린더입력", "주조압력"], keep="last"))


print(ln1)
