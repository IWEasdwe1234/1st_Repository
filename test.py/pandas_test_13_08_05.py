# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 5. 위험 순으로 정렬하기")
# 실습 5. 위험 순으로 정렬하기

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 목표
# 데이터를 위험한 순서로 정렬하고 상위만 추출

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
print("== df.info() 실행 ==\n")
print(df.shape)
df.info()
print(df.head(3))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 단계
# sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
print("== 비스킷두께를 큰 값부터 내림차순 정렬 ==\n")
print(df.sort_values("비스킷두께", ascending=False))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# head로 상위 다섯 개만 추출해 값 확인
print("== 상위 다섯 개만 추출 ==")
print(df.sort_values("비스킷두께", ascending=False).head(5))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 여러 열을 리스트로 묶어 우선순위 다중 정렬
print("== 우선순위 다중 정렬 ==")
df_multi = df.sort_values(["품질등급", "형체력"], ascending=[True, False])
print(df_multi.head(5))
