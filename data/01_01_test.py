# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)

tag = "PL1-SNT-FAN-01-VIB"
# 공장-공정-설비-일련번호-계측값

parts = tag.split("-")

# "-"기준으로 나눈 결과 문자열을 변수에 따로 저장
plant = parts[0]  # 공장
process = parts[1]  # 공정
equip = parts[2]  # 설비
unit_no = parts[3]  # 일련번호
measure = parts[4]  # 측정항목


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

MEASURE_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}


import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")


# 공정별로 몇 개의 태그가 있는지 세어보기
split_cols = df["tag"].str.split("-", expand=True)
df["plant"] = split_cols[0]
df["process"] = split_cols[1]
df["equip"] = split_cols[2]
df["unit_no"] = split_cols[3]
df["measure"] = split_cols[4]

df["process_kr"] = df["process"].map(PROCESS_KR)


# 실습1.
# 24개 태그를 읽어 공정과 상하공정 구분을 판정한 표 작성
# 공정별로 묶어 태그가 가장 많은 공정 확인
# 계측 항목별로 묶어 가장 많은 물리량 확인

# 1. 상·하공정 구분
PROCESS_TYPE = {
    "SNT": "상공정",
    "CKO": "상공정",
    "BF": "상공정",
    "BOF": "상공정",
    "CCM": "상공정",
    "HSM": "하공정",
    "CRM": "하공정",
    "ULT": "지원공정",
}

df["process_type"] = df["process"].map(PROCESS_TYPE)

# 공정과 상·하공정 구분 결과 확인
print(df[["tag", "process_kr", "process_type"]])


print(ln2)


# 2. 공정별 태그 개수
process_count = df.groupby("process_kr").size().sort_values(ascending=False)

print("공정별 태그 개수")
print(process_count)

print("가장 많은 공정:", process_count.idxmax())
print("태그 개수:", process_count.max())


print(ln2)


# 3. 계측 항목별 태그 개수
df["measure_kr"] = df["measure"].map(MEASURE_KR)

measure_count = df.groupby("measure_kr").size().sort_values(ascending=False)

print("계측 항목별 태그 개수")
print(measure_count)

print("가장 많은 물리량:", measure_count.idxmax())
print("태그 개수:", measure_count.max())

print(ln1)
