# 리스트 데이터 처리
print("\n== 리스트 데이터 처리 ==")

# 실습1. 조건에 맞는 값만 출력하기
print("\n실습1. 조건에 맞는 값만 출력하기")

num = [32, 27, 31, 28, 35, 29, 31]

for n in num:
    if n >= 30:
        print("고온:", n)


# 실습2. 두 조건을 모두 만족하는 값 고르기
print("\n실습2. 두 조건을 모두 만족하는 값 고르기")

tl = [4, 8, 2, 3, 6, 10, 9]
for n in tl:
    if n >= 5 and n <= 10:
        print(n)


# 실습3. 조건에 맞는 값만 골라 평균 구하기
print("\n실습3. 조건에 맞는 값만 골라 평균 구하기")
# 리스트 = 5 이상

temps = [29, 32, 25, 24, 36, 31]
A = 0
B = 0
for n in temps:
    if n > 30:
        A += n
        B += 1
print("고온 평균:", A / B)

# --------------
print("\n ------- ")
# 기존 배열의 모든 요소에 3을 곱한 값을 리스트로 출력

temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []

for t in temps:
    doubled.append(t * 3)

print(doubled)


print("\n")

# 조건에 맞는 값으로 세 리스트 만들기
# temps = [1, 5, 2, 7, 4, 8, 10, 3]
high = []
low = []

for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)

print("high: ", high)
print("low: ", low)

# 복습) sort(): 원본 배열을 오름차순으로 정렬해줌
# 하지만 반환해주지 않기 때문에 print로 바로 찍으면 None 출력
print(low.sort())  # None

# 정렬된 배열을 출력하고 싶다면 아래처럼
low.sort()
print(low)


# 실습4. 조건에 맞는 값으로 새 리스트 만들기
print("\n실습4. 조건에 맞는 값으로 새 리스트 만들기")
temps = [21, 32, 27, 35, 31, 26, 33]
lst = []

for n in temps:
    if n > 30:
        lst.append(n)
print(lst)
print("개수", len(lst))

# ========================================

# 실습5. 값을 가공해 새 리스트 만들기
print("\n실습5. 값을 가공해 새 리스트 만들기")

temps_C = [30, 32, 37, 40, 31]
temps_F = []

for t in temps_C:
    temps_F.append(round(t * 1.8 + 32, 1))
print(temps_F)


# ========================================

# 리스트 안의 리스트
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 리스트를 "열"

print(rows[0])
print(type(rows[0]))  # <class 'list'>
print(type(rows))  # <class 'list'>
# 중첩된 리스트 안의 값에 접근
print(rows[1][1])
# 1. rows[1]을 찾음 -> ["모터", 32]
# 2. print(["모터", 32][1]) -> [1] 앞의 리스트에서 1번 인덱스 값에 접근
# 3. print(32) -> 32 출력
# 중첩된 리스트 내부의 값은 대괄호를 여러번 이어서 접근

print("\n")

print("리스트 안의 리스트 온도값만 출력하기")
# 리스트 안의 리스트 온도값만 출력하기
for row in rows:
    print(row[0], "온도", row[1])  # 펌프 온도 25
# rows는 리스트를 담고 있는 큰 리스트
# row는 rows 안에 있는 작은 리스트 예) ["펌프", 23] 하나

print("\n")

# 실습6. 센서 데이터 종합 분석하기
print("\n실습6. 센서 데이터 종합 분석하기")

temps = [30, 32, 37, 40, 31]
rs1 = 0

for t in temps:
    rs1 += t
print("전체 평균:", rs1 / len(temps))

rs2 = []
for t in temps:
    if t > 30:
        rs2.append(t)
total = 0
for n in rs2:
    total += n
print("고온 개수:", len(rs2))
print("고온 평균:", total / len(rs2))
