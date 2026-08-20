# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 4. 통합 리포트 종합")
# 실습 4. 통합 리포트 종합

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")


import pandas as pd

df = pd.read_csv("data/14_equipment_sensor.csv", encoding="utf-8")
df.info()

# 목표
# 그룹 통계와 상관 분석을 묶어 발견·해석·행동 리포트 구성


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 단계
# 라인(line)으로 그룹을 나눠 (temp의) 측정수(count)·평균온도(mean)·온도편차(std) 요약
# -> agg
print("== 측정수·평균온도·온도편차 요약 ==\n")
report = df.groupby("line")["temp"].agg(["count", "mean", "std"]).round(2)
print(report)
#       count   mean    std
# line
# A라인      54  76.86  10.18
# B라인      35  77.69   7.60
# C라인      31  79.88  10.38

# 위 결과를 그대로 복사해서 보고서에 붙여넣기하면 다른 사람은 알아보기 어렵다
# 그래서 label 처리를 해주는게 좋다. (Pandas 권장사항)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

print("== label 처리 ==\n")
report = (
    df.groupby("line")
    .agg(측정수=("temp", "count"), 평균온도=("temp", "mean"), 온도편차=("temp", "std"))
    .round(2)
)
print(report)
#       측정수   평균온도   온도편차
# line
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60
# C라인    31  79.88  10.38

# 표 안에서도 심각한 정보를 먼저 보여주는 게 필요하다.
# 이 경우에는 온도편차가 큰 경우가  심각한 정보라서 우선 나타나게 해주자

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

print("== 심각한 정보 우선 처리 ==\n")
print(report.sort_values("온도편차", ascending=False))
#       측정수   평균온도   온도편차
# line
# C라인    31  79.88  10.38
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 온도(temp)와 진동(vibration)의 상관계수(corr)를 구해 함께 움직임 확인
print("== 온도와 진동의 상관계수 ==\n")
r = df["temp"].corr(df["vibration"])
print(r.round(3))  # 0.345

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 고장(result == 고장) 행을 걸러 라인별 고장 건수까지 더해 우선 점검 대상 정리
print("== 온도와 진동의 상관계수 ==\n")
df_bad = df[df["result"] == "고장"]
print(df_bad.head(2))
#   line shift machine  temp  vibration  pressure result
# 3  B라인    주간     M02  75.0       2.29      5.55     고장
# 4  A라인    주간     M03  71.7       3.66      5.85     고장

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
print(f"\n{"~ " * 15}\n")

print("-- 라인별 고장 건수 --\n")
print(df_bad.groupby("line").size())
# line
# A라인    16
# B라인     6
# C라인     6

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
