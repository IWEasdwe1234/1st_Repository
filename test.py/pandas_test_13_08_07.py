# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

print("실습 7. 이상 의심 설비 리포트")
# 실습 7. 이상 의심 설비 리포트

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

import pandas as pd

# 목표
# 불러오기부터 판단 문장까지 전체 워크플로우를 두 데이터에 적용

# 1. 불러오기
print("== 1. 불러오기 ==\n")
df = pd.read_csv("data/13_diecasting_shot.csv")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 2. 확인하기
print("== 2. 확인하기 ==\n")
df.info()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 3. 필터링
print("== 3. 필터링 ==\n")
df_warning = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 100)]
print(len(df_warning))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 4. 정렬
print("== 4. 정렬 ==\n")
df_report = df_warning.sort_values("비스킷두께", ascending=False)
print(df_report.head())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")

# 5. 선택 : [[...]]대괄호 중첩 주의
print("== 5. 선택 ==\n")
df_final = df_report[["샷", "품질등급", "형체력", "사이클타임"]]
print(df_final.head())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~ " * 15}\n")

print("가장 위험 목록\n")
print(df_final.head())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~ " * 15}\n ")

df_danger = df_final.head(1)
print("가장 위험 항목\n")
print(df_danger)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")


# 단계
# 복합 조건으로 위험 설비를 거르고 비스킷두께내림차순 정렬
print("== 복합 조건으로 위험 설비를 거르고 비스킷두께내림차순 정렬 ==\n")
df_warning = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 100)]

df_report = df_warning.sort_values("형체력", ascending=False)
print(df_report.head())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~ " * 15}\n ")

# 필요한 주요 열만 선택하고 가장 위험한 설비로 판단 문장 작성
print("== 필요한 주요 열만 선택하고 가장 위험한 설비로 판단 문장 작성 ==\n")
df_final = df_report[["샷", "품질등급", "형체력", "사이클타임"]]

df_danger = df_final.head(1)

sid = int(df_danger["샷"].tolist()[0])
force = df_danger["형체력"].tolist()[0]

print(f"가장 시급한 샷: {sid}번, 형체력 {force}, 우선 점검")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~ " * 15}\n ")

# 같은 흐름을 주조 로그 불량 데이터에도 적용해 결과 비교
print("== 같은 흐름을 주조 로그 불량 데이터에도 적용해 결과 비교 ==\n")
df_bad = df[df["품질등급"] == "불량"].sort_values("형체력", ascending=False)

print(df_bad[["샷", "형체력"]].head())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n{"~" * 30}\n")
