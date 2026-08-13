# 실습 4. loc와 iloc로 행 선택하기 ==
print("실습 4. loc와 iloc로 행 선택하기 ==")

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

# 목표
# 라벨 기준 loc와 번호 기준 iloc로 행 선택, 범위 차이 확인


# 단계
# loc로 라벨 기준 단일 행 선택
print('\ndf.loc[0, "품질등급"] 출력\n')
print(df.loc[0, "품질등급"])  # 양품

# ----------------------------------------
print(f"\n{"-" * 40}\n")

# iloc로 번호 기준 단일 행 선택
# df.iloc[0] -> 특정 row number인 row의 Serise 추출
# ..["품질등급"] -> 해당 Serise에서 "품질등급" 컬럼의 내용만 추출
print('df.iloc[0]["품질등급"] 출력\n')
print(df.iloc[0]["품질등급"])  # 양품

# ----------------------------------------
print(f"\n{"-" * 40}\n")

# 범위 선택으로 loc 끝 포함·iloc 끝 제외 차이 확인
# 다음 두 줄의 결과는 각각 어떻게 나타나는지
# 두 결과는 동일한지 아니면 다른지를 주석으로 달아주세요
print("len(df.loc[0:2]) 출력\n")
print(len(df.loc[0:2]))  # 3

print("\nlen(df.iloc[0:2]) 출력\n")
print(len(df.iloc[0:2]))  # 2
