# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)

tag = "PL1-SNT-FAN-01-VIB"
# 공장-공정-설비-일련번호-계측값

parts = tag.split("-")
print(parts)

print(ln2)
# "-"기준으로 나눈 결과 문자열을 변수에 따로 저장
plant = parts[0]  # 공장
process = parts[1]  # 공정
equip = parts[2]  # 설비
unit_no = parts[3]  # 일련번호
measure = parts[4]  # 측정항목

print(plant, process, equip, unit_no, measure)
# PL1 SNT FAN 01 VIB

print(ln2)

PROCESS_KR = {
    "SNT": "소결",
    "CKO": "코크스",
    "BF": "고로",
    "BOF": "전로",
    "CCM": "연주",
    "HSM": "열간압연",
    "CRM": "냉간압연",
    "ULT": "유틸리티",
}

# 전로를 출력하려면?(BOF 키)
print(PROCESS_KR["BOF"])

# 없는 태글르 가져오는 것 방지
print(PROCESS_KR.get("BOF1", "미등록"))

print(ln2)

MEASURE_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

print(MEASURE_KR.get("PRS", "미등록"))

print(ln1)

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")
print(df.shape)  # (24, 4)
print(df.columns.tolist())  # ['tag', 'unit', 'sample_value', 'note']

print(ln2)

# 공정별로 몇 개의 태그가 있는지 세어보기
split_cols = df["tag"].str.split("-", expand=True)
df["plant"] = split_cols[0]
df["process"] = split_cols[1]
df["equip"] = split_cols[2]
df["unit_no"] = split_cols[3]
df["measure"] = split_cols[4]

print(df.loc[0, "process"], df.loc[0, "measure"])

print(ln2)

df["process_kr"] = df["process"].map(PROCESS_KR)
print(df[["tag", "process_kr"]].head(3))

print(ln2)

print(df.groupby("process_kr").size())

# 예시 결과
# 고로 N
# 냉간압연 M
# .... (8행)


# # 개인 실습 코드
# df["process"] = df["tag"].str.split("-").str[1]

# # 공정 코드를 한글명으로 변경
# df["process"] = df["process"].replace(PROCESS_KR)

# # 공정별 태그 개수
# process_count = df["process"].value_counts()

# print(process_count)

print(ln1)


# 실습1.
# 24개 태그를 읽어 공정과 상하공정 구분을 판정한 표 작성
# 공정별로 묶어 태그가 가장 많은 공정 확인
# 계측 항목별로 묶어 가장 많은 물리량 확인


MEASURE_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

MEASURE_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

STAGE_KR = {
    "SNT": "상공정",
    "CKO": "상공정",
    "BF": "고로",
    "BOF": "상공정",
    "CCM": "상공정",
    "HSM": "하공정",
    "CRM": "하공정",
    "ULT": "유틸리티",
}

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")
print("전체 행수:", len(df))  # 24
df[["plant", "process", "equip", "unit_no", "measure"]] = df["tag"].str.split(
    "-", expand=True
)

print(ln2)
print(df.head())

df["process_kr"] = df["process"].map(PROCESS_KR).fillna("미등록")
df["measure_kr"] = df["measure"].map(MEASURE_KR).fillna("미등록")

print(df.head())

print(ln1)

# (문제 1번)상공정, 하공정과 관련된 stage 컬럼 추가
df["stage"] = df["process"].map(STAGE_KR).fillna("alemdfhr")
print(df.head())
print(df.groupby("stage").size())

print(ln2)
# (문제 3번) 계측항목별 태그개수와 가장 많이 등장하는 물리량(계측항목) 출력해보기
measure_a = df.groupby("measure_kr").size().sort_values(ascending=False, kind="stable")
print(measure_a.idxmax())

print(ln2)
measure_b = df.groupby("measure_kr").size()
print(measure_b)

print(ln1)

# 참고
# <실습1>

# import pandas as pd

# PROCESS_KR = {
#     "SNT": "소결",
#     "CKO": "코크스",
#     "BF": "고로",
#     "BOF": "전로",
#     "CCM": "연주",
#     "HSM": "열간압연",
#     "CRM": "냉간압연",
#     "UTL": "유틸리티",
# }
# MEASURE_KR = {
#     "VIB": "진동",
#     "CUR": "전류",
#     "TMP": "온도",
#     "PRS": "압력",
#     "FLW": "유량",
#     "SPD": "속도",
#     "LVL": "레벨",
# }

# # 공정별 하공정, 상공정 분류
# STAGE_KR = {
#     "SNT": "상공정",
#     "CKO": "상공정",
#     "BF": "상공정",
#     "BOF": "상공정",
#     "CCM": "상공정",
#     "HSM": "하공정",
#     "CRM": "하공정",
#     "UTL": "유틸리티",
# }

# # 데이터 읽기
# df = pd.read_csv("01-01_철강_공정_개관_설비태그.csv")
# print("전체 행수:", len(df)) # 24

# # dataframe 에 태그에 포함되어있는 정보 컬럼을 추가하기
# # df의 tag를 '-' 기준으로 잘라서 각 컬럼에 순서대로 저장
# df[["plant", "process","equip", "unit_no", "measure"]] = df["tag"].str.split("-", expand=True)

# print(df.head())

# # map을 통해서 딕셔너리의 키와 (process, measure) 연결
# df["process_kr"]=df["process"].map(PROCESS_KR).fillna("미등록")
# df["measure_kr"]=df["measure"].map(MEASURE_KR).fillna("미등록")

# print(df.head())

# # (문제 1번) 상공정, 하공정과 관련된 stage 컬럼 추가 
# df["stage"]=df["process"].map(STAGE_KR).fillna("미등록")
# print(df.head())

# # groupby: stage 별로 같은 값을 가진 행끼리 묶고
# # size: 개수세기
# print(df.groupby("stage").size())
# '''
# stage
# 상공정     14
# 유틸리티     3
# 하공정      7
# '''

# # (문제 3번) 계측항목별 태그개수와 가장 많이 등장하는 물리량(계측항목) 출력해보기
# measure_a=df.groupby("measure_kr").size().sort_values(ascending=False, kind="stable")

# #idxmax(): 시리즈나 데이터프레임에서 최대값을 가진 인덱스를 반환
# print(measure_a.idxmax())

# ###### sort_values()의 kind옵션 - 어떤 정렬 알고리즘 사용할지 지정
# # stable: 값이 같은 경우 기존 순서를 유지하는 정렬 (안정 정렬)
# # quicksort: 퀵정렬 사용하여 정렬 
# # mergesort: 병합정렬 사용하여 정렬 
# # heapsort: 힙정렬 사용하여 정렬
# measure_b=df.groupby("measure_kr").size()
# print(measure_b) # 정렬X
# print('-------')

# print(measure_a) # 정렬O