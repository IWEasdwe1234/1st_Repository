ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)

# 앞 6시간과 뒤 6시간 비교

# 목표
# 정상 구간과 변화구간의 평균을 비교합니다.

# 요구사항
# 앞 6시간과 뒤 6시간으로 나누어 아래 평균을 비교하세요

# - 송풍량
# - 송풍압
# - 송풍기 진동

# 세 값의 변화 방향을 각각적으세요.

# 제출물
# 앞/뒤 6시간 평균 비교표와 변화 방향 3개

# 사용할 수 있는 힌트
# before = df.iloc[:360]
# after = df.iloc[360:0]

# cols = ["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]

# befor[cols].mean()
# after[cols].mean()


import pandas as pd

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")

# 앞 6시간, 뒤 6시간
before = df.iloc[:360]
after = df.iloc[360:]

# 앞/뒤 6시간 송풍량, 송풍압, 송풍기 진동의 평균
cols = ["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]
print(before[cols].mean().round(2))
print(ln2)
print(after[cols].mean().round(2))
# blast_flow_nm3min     5198.67
# blast_pressure_kpa     379.79
# blower_vib_mms           3.40

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# blast_flow_nm3min     4977.83
# blast_pressure_kpa     397.72
# blower_vib_mms           3.40

# 송풍량 : 5198.67 -> 4977.83 (약 200 하향)
# 송풍압 : 379.79 -> 397.72 (약 20 상승)
# 송풍기 진동 : 3.40 -> 3.40 (변동 없음)

print(ln1)
