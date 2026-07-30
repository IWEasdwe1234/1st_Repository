# while문
print("\n== while문 ==")
# 반복해야 하는 경우 사용

# 무한루프 유의
# count = 1
# while count <=3:
#   print(count) > 무한 루프 발생
#   while문은 조건이 거짓이 되는 플래그를 꼭 세워야 함

# 무한루프의 강제 종료 : Ctrl+C

# while문 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지

count = 1  # 1번

while count <= 3:  # 2번
    # count = 0  # 반복문 안에 count 변수를 계속 0으로 재할당해서 무한루프에 빠짐
    print(count)
    count += 1  # 3번

# - 실습1.while로 목표값 도달까지 반복하기 -
print("\n- 실습1.while로 목표값 도달까지 반복하기 -")

ans = 7
user = 0

while user != ans:
    user = int(input("목표값 입력: "))
    print("아직 목표값이 아니다")
print("정답입니다!")


# - break -
print("\n- break -")

# 반복을 그만 돌고 싶을 때
# 예1) [1,1,3,3,2,1,1,1]
# 위 리스트를 돌면서 10 이상이 되면 중단하고 싶을 때
# 예2) 사용자 입력값을 누적하다가 누적값이 총 15를 넘으면
# 종료하고 싶을 때
# break 사용 시 즉시 for문을 나감

# 예시2)
print("\n예시2)")

input_sum = 0

while True:  # 조건만 보면 무한반복하는 코드
    user_input = int(input("값을 입력하세요. 값의 누적이 15를 넘으면 종료합니다: "))
    input_sum += user_input  # 누적값 업데이트

    if input_sum > 15:  # 종료 트리거
        print("누적 합계:", input_sum, "입력을 종료합니다.")
        break  # 합계가 15를 넘으면 반복 종료
print("break를 통해 while문을 나가면 이후 코드가 실행됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
while True:
    # 변수 x는 반복을 돌 때마다 재할당되기 때문에 휘발되지만
    x = input("입력 (종료는 Q를 입력하세요): ").lower()
    # 현재 입력값이 뭔지는 확인할 수 있음
    if x == "q":
        break
    print("입력받은 값:", x)


# ========================
print("\n==================")
print("\n반복 속 조건 분기")

n = int(input("횟수: "))

for i in range(n):
    v = int(input("측정값: "))

    if v > 80:
        print("이상 발생")
        print("가동 횟수:", n)
        break
    else:
        print("정상 상태")


# 실습 up down 게임
print("\n실습 up down 게임)")
# 1~50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 출력

ans = 24
num = 0

while num != ans:
    num = int(input("\n1~50 중 하나의 숫자 입력: "))
    if num < ans:
        print("up")
    elif num > ans:
        print("down")
    else:
        print("정답, 게임이 종료되었습니다.")
        break


# ========================
print("\n==================")
print("\n최댓값, 최솟값 찾기")

# 최댓값 찾기
print("\n - 최댓값 -")
first = int(input("1번째 입력값: "))

# 첫 번째 입력값은 자동으로 최댓값이 됨 (비교할 다른 값이 없기 때문)
max_value = first

# for문을 사용해서 사용자 입력을 4번 받고
# 입력 받은 값 중에서 가장 큰 값을 출력
for i in range(4):
    v = int(input(f"{i+2}번째 입력: "))
    # 위에서 1번째 입력을 받고, i는 0부터 시작하기 때문에 2를 더해서 출력

    # max_value에는 현 시점 최댓갑
    # v에는 방금 사용자가 입력한 값
    # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
    if v > max_value:
        max_value = v
print("최댓값:", max_value)  # for 반복문 종료 후 최종 최댓값 출력

# ========================

print("\n==================")
print("\n흐름 표를 보고 코드 작성")

total = 0

for i in [4, 7, 6]:
    if i > 5:
        total += i
print("합계:", total)

# ========================

# 실습2. 플래그로 조건 만족 값 검색하기
print("\n실습2. 플래그로 조건 만족 값 검색하기")

num = int(input("횟수: "))
fnd = False
for i in range(n):
    v = int(input("측정값: "))
    if v > 80:
        fnd = True
        break
if fnd:
    print("발견")
else:
    print("없음")


# ========================

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
