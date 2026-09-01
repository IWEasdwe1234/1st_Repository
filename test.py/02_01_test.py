# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln1 = f"\n{"~" * 30}\n"
ln2 = f"\n{"~ " * 10}\n"
print(ln1)


import pandas as pd

df = pd.read_csv("data/02-01_측정의_3요소_설비태그목록.csv")
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 16 entries, 0 to 15
# Data columns (total 8 columns):
#  #   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   tag               16 non-null     str
#  1   description       16 non-null     str
#  2   unit              16 non-null     str
#  3   sampling_sec      16 non-null     int64
#  4   range_min         16 non-null     int64
#  5   range_max         16 non-null     int64
#  6   resolution        16 non-null     float64
#  7   install_location  16 non-null     str
# dtypes: float64(1), int64(3), str(4)

print(ln1)
# 컬럼명 한글화
df = df.rename(
    columns={
        "tag": "태그명",
        "description": "물리",
        "unit": "단위",
        "install_location": "설치 위치",
        "sampling_sec": "사양 주기(초)",
    }
)

# 필요한 컬럼
columns = ["태그명", "물리", "단위", "설치 위치", "사양 주기(초)"]

# CASE A
case_a = df[df["태그명"].str.startswith("MTR")]

print("==[ CASE A ]==")
print(case_a[columns].to_string(index=False))

print(ln2)

# CASE B
case_b = df[df["태그명"].str.startswith(("HYD", "FUR"))]

print("\n==[ CASE B ]==")
print(case_b[columns].to_string(index=False))


print(ln1)

# 실행 결과

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# <class 'pandas.DataFrame'>
# RangeIndex: 16 entries, 0 to 15
# Data columns (total 8 columns):
#  #   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   tag               16 non-null     str
#  1   description       16 non-null     str
#  2   unit              16 non-null     str
#  3   sampling_sec      16 non-null     int64
#  4   range_min         16 non-null     int64
#  5   range_max         16 non-null     int64
#  6   resolution        16 non-null     float64
#  7   install_location  16 non-null     str
# dtypes: float64(1), int64(3), str(4)
# memory usage: 1.1 KB

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ==[ CASE A ]==
#             태그명                   물리   단위           설치 위치  사양 주기(초)
# MTR01_VIB_RMS_H  1번 모터 구동측 수평 진동 실효값 mm/s  구동측 베어링 하우징 수평        60
# MTR01_VIB_RMS_V  1번 모터 구동측 수직 진동 실효값 mm/s  구동측 베어링 하우징 수직        60
# MTR01_VIB_RMS_A 1번 모터 구동측 축방향 진동 실효값 mm/s 구동측 베어링 하우징 축방향        60
#   MTR01_VIB_ACC    1번 모터 비구동측 진동 가속도    g    비구동측 베어링 하우징        60
#   MTR01_CURRENT          1번 모터 운전 전류    A   모터 제어반 전류 변성기        60
#      MTR01_VOLT          1번 모터 입력 전압    V    모터 제어반 전압 단자        60
#     MTR01_POWER     1번 모터 소비 전력(계산값)   kW  계산값 - 전압×전류 기반        60
#      MTR01_TEMP      1번 모터 고정자 권선 온도 degC 고정자 권선 매입 측온저항체        60
#       MTR01_RPM        1번 모터 회전수 rpm  rpm       축단 회전수 센서        60

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~


# ==[ CASE B ]==
#             태그명                물리    단위             설치 위치  사양 주기(초)
#  HYD01_PRESS_IN    1번 유압 유닛 공급 압력   bar          펌프 토출 배관        60
# HYD01_PRESS_OUT 1번 유압 유닛 필터 후단 압력   bar          필터 후단 배관        60
# HYD01_DP_FILTER  1번 유압 필터 차압(계산값)   bar 계산값 - 공급압력 - 후단압력        60
#      HYD01_FLOW 1번 유압 유닛 펌프 토출 유량 L/min      펌프 토출 배관 유량계        60
#   HYD01_OILTEMP   1번 유압 유닛 작동유 온도  degC          유압 탱크 내부       300
#   FUR01_TEMP_Z1  1번 가열로 1존 분위기 온도  degC         1존 천장 열전대       300
#   FUR01_TEMP_Z2  1번 가열로 2존 분위기 온도  degC         2존 천장 열전대       300

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
