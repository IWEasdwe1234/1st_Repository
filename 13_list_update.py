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
