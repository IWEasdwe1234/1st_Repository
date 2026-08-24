# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln0 = f"\n{"== " * 15}\n"
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"

import pandas as pd

CD = "data/16_diecasting.csv"
WD = "data/16_welding.csv"

df = pd.read_csv(CD)


# 실습 6. 처리 전후 통계 비교
print(ln1 + "\n" + ln0 + "\n실습 6. 처리 전후 통계 비교\n" + ln0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 제거·보정·중앙값 채움 세 처리의 평균 변화 비교

# 목표
# 제거·보정·중앙값 채움 세 처리의 평균 변화 비교

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# 실린더압력 이상치 경계와 조건을 만들기
print(ln1 + "\n==[ 실린더압력 이상치 경계와 조건을 만들기 ]==\n")
Q1 = df["실린더압력"].quantile(0.25)
Q3 = df["실린더압력"].quantile(0.75)
IQR = Q3 - Q1
L = Q1 - 1.5 * IQR
U = Q3 + 1.5 * IQR

m = (df["실린더압력"] < L) | (df["실린더압력"] > U)
채움 = df["실린더압력"].mask(m).fillna(df["실린더압력"].mask(m).median())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 제거·보정·중앙값 채움 세 방식을 각각 적용
print(ln1 + "\n==[ 제거·보정·중앙값 채움 세 방식을 각각 적용 ]==\n")
df.loc[~m, "실린더압력"]  # 제거
df["실린더압력"].clip(L, U)  # 보정
df["실린더압력"].mask(m).fillna(df["실린더압력"].mask(m).median())  # 중앙값 채움

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 처리 전 평균과 세 방식의 평균을 나란히 비교
print(ln1 + "\n==[ 처리 전 평균과 세 방식의 평균을 나란히 비교 ]==\n")
print(round(df["실린더압력"].mean(), 2))  # (처리전)
print(round(df[~m]["실린더압력"].mean(), 2))  # (mask로 제거)
print(round(df["실린더압력"].clip(L, U).mean(), 2))
print(round(채움.mean(), 2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 실습 7. duplicated로 중복 찾기와 개수
print(ln1 + "\n" + ln0 + "\n실습 7. duplicated로 중복 찾기와 개수\n" + ln0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 완전 중복 행을 찾고 keep 옵션으로 개수 비교

# 목표
# 완전 중복 행을 찾고 keep 옵션에 따른 개수 비교

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# duplicated로 중복 행 여부를 참·거짓으로 표시
print(ln1 + "\n==[ duplicated로 중복 행 여부를 참·거짓으로 표시 ]==\n")
print(df.duplicated())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# sum으로 중복 개수 세고 중복 행 직접 확인
print(ln1 + "\n==[ sum으로 중복 개수 세고 중복 행 직접 확인 ]==\n")
print(df.duplicated().sum())
print(df[df.duplicated()])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인
print(ln1 + "\n==[ keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인 ]==\n")
print(df.duplicated(keep=False).sum())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 실습 8. drop_duplicates로 중복 제거
print(ln1 + "\n" + ln0 + "\n실습 8. drop_duplicates로 중복 제거\n" + ln0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 완전 중복 제거와 기준 컬럼 제거를 비교

# 목표
# 완전 중복 제거와 기준 컬럼 지정 제거를 비교

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# drop_duplicates로 완전 중복 행 제거
print(ln1 + "\n==[ drop_duplicates로 완전 중복 행 제거 ]==\n")
df_onlyone = df.drop_duplicates()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 제거 후 행 수와 남은 중복 개수 확인
print(ln1 + "\n==[ 제거 후 행 수와 남은 중복 개수 확인 ]==\n")
print(len(df))  # 제거 전
print(len(df_onlyone))  # 제거 후


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# subset으로 특정 컬럼만 기준 삼아 제거
print(ln1 + "\n==[ subset으로 특정 컬럼만 기준 삼아 제거 ]==\n")
df_onlyone_shot = df.drop_duplicates(subset=["샷"], keep="last")
print(len(df_onlyone_shot))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 실습 9. reset_index로 인덱스 정리
print(ln1 + "\n" + ln0 + "\n실습 9. reset_index로 인덱스 정리\n" + ln0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 중복 제거로 생긴 인덱스 구멍을 다시 매기기

# 목표
# 중복 제거로 생긴 인덱스 구멍을 0부터 다시 매기기

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# drop_duplicates로 중복을 제거
print(ln1 + "\n==[ drop_duplicates로 중복을 제거 ]==\n")
df_clean = df.drop_duplicates()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# reset_index로 인덱스를 0부터 다시 매기기
print(ln1 + "\n==[ reset_index로 인덱스를 0부터 다시 매기기 ]==\n")
df_clean_idxreset = df_clean.reset_index(drop=True)

print(df_clean.index.min(), df_clean.index.max())
print(len(df_clean))

print(df_clean_idxreset.index.min(), df_clean_idxreset.index.max())
print(len(df_clean_idxreset))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 인덱스 최솟값·최댓값으로 연속성 확인
print(ln1 + "\n==[ 인덱스 최솟값·최댓값으로 연속성 확인 ]==\n")
print("인덱스 최솟값 :", df_clean_idxreset.index.min())
print("인덱스 최댓값 :", df_clean_idxreset.index.max())
print("데이터 개수 :", len(df_clean_idxreset))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 실습 10. 다른 현장(용접) 이상치·중복 종합 정제
print(ln1 + "\n" + ln0 + "\n실습 10. 다른 현장(용접) 이상치·중복 종합 정제\n" + ln0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 탐색→보정→중복 점검→저장을 다른 현장에 그대로


# 목표
# IQR 탐색부터 정제 데이터 저장까지 한 흐름으로

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 단계
# 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인
print(ln1 + "\n==[ 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인 ]==\n")
wf = pd.read_csv(WD)
c = "통전전류"

q1, q3 = wf[c].quantile(0.25), wf[c].quantile(0.75)
lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
m = (wf[c] < lo) | (wf[c] > hi)
print(int(m.sum()), round(m.mean() * 100, 1))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# clip으로 이상치를 보정하고 중복을 제거·정리
print(ln1 + "\n==[ clip으로 이상치를 보정하고 중복을 제거·정리 ]==\n")
wf[c] = wf[c].clip(lower=lo, upper=hi)
wf = wf.drop_duplicates().reset_index(drop=True)
print(len(wf))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 정제한 데이터를 파일로 저장
print(ln1 + "\n==[ 정제한 데이터를 파일로 저장 ]==\n")
wf.to_csv("data/16_welding_cleaned.csv", index=False)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
