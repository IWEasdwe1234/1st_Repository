# ========================================
# 종합 실습 1. 설비 종합 모니터링 리포트


print("\n\n========================================")
print("        설비 종합 모니터링 리포트")
print("========================================")


# (설비명, 온도, 진동)
# (name, temp, vib)
sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험 🚨"
#   온도 >= 80 또는 진동 >= 3.0 > "주의 ⚠️"
#   그 외                      > "정상 ✅"


# ========================================

# 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력
# (for + enumerate + if/elif/else)

normal = 0
Warning = 0
danger = 0

temp_sum = 0

max_temp = 0
max_name = ""

danger_list = []

for i, sensor in enumerate(sensors, start=1):
    name = sensor[0]
    temp = sensor[1]
    vib = sensor[2]

    temp_sum += temp

    if temp > max_temp:
        max_temp = temp
        max_name = name
    if temp > 90 or vib > 5.0:
        state = "위험 🚨"
        danger += 1
        danger_list.append(name)

    elif temp >= 80 or vib > 3.0:
        state = "주의 ⚠️"
        Warning += 1
    else:
        state = "정상 ✅"
        normal += 1

    print(f"{i}. {name} | 온도 {temp}℃ | 진동 {vib}mm/s | {state}")


# ----------------------------------------
print("----------------------------------------")

# 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)

print(f"정상: {normal} / 주의: {Warning} / 위험: {danger}")


# 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)
rst1 = round((Warning + danger) / len(sensors) * 100, 1)
print(f"이상 설비 비율: {rst1}%")


# 4. 전체 평균 온도 출력 (round)
rst2 = round(temp_sum / len(sensors), 1)
print(f"평균 온도: {rst2}℃")


# 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)
print(f"최고 온도 설비: {max_name} ({max_temp}℃)")


# 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())
danger_list.sort()
print("위험 설비 목록:", danger_list)

# ========================================
print("========================================")
