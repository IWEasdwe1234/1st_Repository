# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)


import pandas as pd

### 1. csv에서 datetime 데이터 불러오기 (to_datetime() 이용)
df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")
print(df.shape)  # (720, 6)

print(ln2)
# timestamp열 데이터타입 확인
print("timestamp의 데이터타입(1) :", df["timestamp"].dtype)
df["timestamp"] = pd.to_datetime(df["timestamp"])
print("timestamp의 데이터타입(2) :", df["timestamp"].dtype)

### 2. read_csv()의 옵션값 이용
df = pd.read_csv(
    "data/01-02_원료_전처리와_제선_제선조업.csv", parse_dates=["timestamp"]
)
print("timestamp의 데이터타입(3) :", df["timestamp"].dtype)

# timestamp의 시간 간격
gaps = df["timestamp"].diff().value_counts()
print(gaps)
# 720행의 데이터 중에서 서로 인접한 719개의 시간 간격이 전부 "0 days 00:01:00"이다
# timestamp
# 0 days 00:01:00    719
# Name: count, dtype: int64

# 송풍량, 송풍압, 송풍기 진동
print(
    df[["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]]
    .describe()
    .round(1)
)

print(ln1)
########## 이동 평균: N분간의 흔들림을 확인하여 송풍량의 장기적인 방향을 보는 지표
# 통기성이 나빠지면 공기가 원료층을 통과하기 어려워져서 실제 들어가는 풍량이 감소할 수 있습니다.
# 15분 간격 이동평균 구하기
df["flow_ma"] = df["blast_flow_nm3min"].rolling(window=15).mean()
print(df["flow_ma"].head(3).tolist())  # [nan, nan, nan]

print(round(df["flow_ma"].iloc[14], 1), round(df["flow_ma"].iloc[400], 1))
# 5201.5 5200.8 << 차이가 크지 않습니다. 이 값으로는 통기성 악화가 보이지 않음
# 현재 csv에서는 송풍량으로 통기성 약화를 확인할 수 없음.

print(ln2)
########## 이동 표준편차
df["top_sd"] = df["top_pressure_kpa"].rolling(window=30).std()
print(round(df["top_sd"].iloc[200], 2), round(df["top_sd"].iloc[560], 2))
# 2.64 4.28
# 같은 노정압 계측, 뒤쪽 구간에서 흔들림이 크게 늘어난 것을 이동 표준편차로 확인할 수 있음.


print(ln1)
