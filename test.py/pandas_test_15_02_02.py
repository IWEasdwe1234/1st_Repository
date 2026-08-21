# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln = f"\n{"~" * 30}\n"
print(ln)

print("실습 2. dropna 옵션 조절")
# 실습 2. dropna 옵션 조절

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# how·thresh·subset로 삭제 기준을 세밀하게 조절

import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")


# 목표
# how·thresh·subset로 삭제 기준을 세밀하게 조절

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# how로 완전히 빈 행만 삭제하는 기준 적용
# -> how = "all"
print("==[ how로 완전히 빈 행만 삭제하는 기준 적용 ]==\n")
print(df.dropna(how="all").shape)  # (250, 22)
# 250개 row가 다 살아남았다는 의미
# : NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# thresh로 값이 일정 개수(예, 20개) "이상"인 행만 남기기
# -> thresh = 20
print('==[ thresh로 값이 일정 개수(예, 20개) "이상"인 행만 남기기 ]==\n')
print(df.dropna(thresh=20).shape)  # (162, 22)
# 250 - 162 = 88개 row는 NaN이 3개 이상이라는 뜻

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)

# subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거
#  -> subset = ["불량여부"]
print("==[ subset으로 특정 컬럼이 빈 행만 삭제 ]==\n")
print(df.dropna(subset=["불량여부"]).shape)  # (250, 22)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(ln)
