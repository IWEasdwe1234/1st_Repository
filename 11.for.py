# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지 않고 반복시킬 수 있음

# for 변수 in range(횟수):
#   반복시킬 코드 (들여쓰기 한 칸 필수)
# 같은 코드를 복사 붙여넣기로 여러번 작성하는 대신
# "N번 실행하라"는 의미

for i in range(3):
    print("안녕하세요!")  # range에 전달한 인자 3만큼 3번 반복
    # for문 안에서 i를 쓰지 않아도 됨 -> 목적이 "3번 반복"일 때

# 0부터 10까지의 숫자 자체가 필요하거나 출력할 때
for i in range(11):
    print(i)
    # i는 증강값을 지정하지 않는 이상 반복할 때마다
    # 자동으로 +1이 적용됨

print("\n")
print("\n0부터 10까지 짝수만 출력")
# 0부터 10까지 짝수만 필요할 때
for i in range(0, 11, 2):  # range(시작, 끝, 증가값)
    print(i)  # 반복할 때마다 i가 2씩 자동으로 증가


# 10까지 홀수만 출력
print("\n10까지 홀수만 출력")

for i in range(1, 11, 2):
    print(i)


# 역순으로 출력
print("\n역순으로 출력")

for v in range(10, 0, -1):
    print(v)


# 10부터 1까지 짝수만 역순으로 출력
print("\n10부터 1까지 짝수만 역순으로 출력")

for v in range(10, 0, -2):
    print(v)

# 동작?
print("\n동작?")
for v in range(0, 10, -2):
    print(v)
# 동작 안함
# 시작값인 0에서 -2를 했을 때 끝 값이 포함되지 않아서 반복문 종료


print("\n")
# 실습1. range로 숫자 흐름 출력하기
print("\n실습1. range로 숫자 흐름 출력하기")

N = int(input("숫자 입력: "))
print("\n1부터 N까지")
for i in range(1, N + 1):
    print(i)
print("\n짝수")
for i in range(2, N + 1, 2):
    print(i)
print("\n음수로 바꿔 N부터 1까지 역순")
for i in range(N, 0, -1):
    print(i)


print("\n실습.3의 배수 출력하기")
# 실습. 3의 배수 출력하기
# 사용자에게 범위를 입력받아 3배수 출력하기
# 예)
#   사용자 입력값: 20
#   출력값: 3, 6, 9, 12, 15, 18
# for문, if문, 나머지연산자
# 3 % 3 == 0인 경우 3의 배수가 됨

num = int(input("숫자 입력: "))

for i in range(1, num + 1):
    if i % 3 == 0:
        print(f"입력한 1~{num}사이 3의 배수 출력: {i}")
    elif i % 5 == 0:
        print(f"입력한 1~{num}사이 5의 배수 출력: {i}")
    # 15와 같이 3의 배수이면서 5의 배수인 경우는 3의 배수라고만 출력

print("\n누적변수")
# for문 안에 누적변수 선언 시

for i in range(1, 6):
    total2 = 0  # 반복을 돌 때마다 새로이 변수에 값이 0으로 할당
    print("total2 = 0 시 total2에 할당된 값:\n", total2)
    print("현재 i의 값:\n", i)
    total2 += i
    print("\n")
    print("total2 += i 후의 total2에 할당된 값:\n", total2)
    # total2 = total2 + i
print("합계: ", total2)  # 가장 마지막 i인 5 출력

print("\n-번외-")
# 번외
if 3 == 3:
    hi = "안녕"
print(hi)  # 안녕
# python에서는 if문 안의 변수도 어디서든 호출 가능한 변수로 선언됨


# 1~15 사이의 4의 배수만 누적
print("\n1~15 사이의 4의 배수만 누적")

total3 = 0
for i in range(1, 16):
    if i % 4 == 0:
        total3 += 3
print("1~15 사이의 4의 배수 누적 결과:", total3)


print("\n")

# enumerate (낱낱이 세다)
print("\nenumerate")

temps = [33, 23, 45, 32, 28]

for t in enumerate(temps):
    print(t)
# (0, 33)
# (1, 23)
# (2, 45)
# (3, 32)
# (4, 28)
# 범위를 지정하지 않아도 enumerate()에 전달한 리스트의 모든 요소 순화
# 문제는 형식이 (인덱스, 해당인덱스요소값)로 출력
# enumerate를 사용할 때는 변수를 2개 전달

print("\n")

for idx, t in enumerate(temps):
    print(f"idx: {idx}, t: {t}")
# idx: 0, t: 33
# idx: 1, t: 23
# idx: 2, t: 45
# idx: 3, t: 32
# idx: 4, t: 28

# for idx, t in enumerate(temps):
# 위와 같이 2개의 변수를 전달하면
# enumerate가 temps 리스트를 순회하면서
# 반환해준 (인덱스, 해당인덱스의값)을
# 각자 idx에 인덱스 값을 할당, t에 해당 인덱스의값을 할당
# 두 개의 값을 바로 사용할 수 있게 해줌


for idx, t in enumerate(temps):
    print(f"현재 인덱스: {idx}")
    print(f"{idx}인덱스의 값: {t}")
    print(f"{idx + 1}번째 반복 끝")

print("\n")

# "안녕"의 인덱스 출력
print('\n"안녕"의 인덱스 출력')
# 이를 위해서는 값을 비교하기 위해 모든 리스트와 값이 필요
# 그리고 그 값의 인덱스를 알아야 출력

list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# 리스트의 모든 요소에 접근을 해야 하는 경우가 잦음
# 그래서 python이 반복문에서 이를 쉽게 할 수 있도록
# enumerate라는 내장 함수를 제공
# enumerate은 리스트의 모든 요소를 앞에서부터
# 순서대로 하나씩 찍어가면서 접근
# 접근해서 각자의 인덱스와 그 값을 뽑아줌 -> 돌려주는 값은 2개()
# 값을 두 개 받으니 우리도 변수를 2개 준비하면
# 각 변수에 쏙쏙 값이 할당
# 돌려주는 순서는 인덱스, 값
# 그렇기 때문에 우리는 enumerate를 사용할 때
# for 뒤에 변수를 두 개 전달

for index, value in enumerate(list):
    print(value)

list_len = int(len(list))
for i in range(list_len):
    print(list[i])

# 사실 이 두가지는 동일한 동작을 함

# =================================

print("\n- 2단 출력 하기 -")
# 2단 출력 하기
for su in range(1, 10):
    print(f"2 X {su} = {2*su}")

# 1~5단 출력하기
# 필요한 변수: 2개 (몇 단을 출력할건지, 거기에 얼마나 곱할건지)
# 몇 단을 출력할건지: 1~5
# 거기에 얼마나 곱할건지: 1~9
# for문 중첩을 사용
# 1단을 유지한 상태에서 곱할 값은 커져야 함
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 1 x 9 = 9
# 2단 시작
# 2 x 1 = 2

# 단수를 유지하고 안에서 또 점점 커지는 변수가 있어야 하니
# 바깥 for문은 단수를 늘리고
# 안쪽 for문은 곱할 수를 늘리도록 구성

print("\n1~5단")
for i in range(1, 6):  # 1~5단까지 반복
    for j in range(1, 10):  # 1단에서 9까지 곱하고 반복 종료
        print(f"{i}X{j}={i*j}")
    print(f"--- {i}단 끝 ---")  # 가장 첫 반복은 1 x 1 = 1

print("\n1~9단 사이 2의 배수 단만 구구단 출력")
# 1~9단 사이 2의 배수 단만 구구단 출력
# 2, 4, 6, 8단만 출력
# range에 간격 전달
# if문 사용

for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 10):
            print(f"{i}X{j}={i*j}")
        print(f"--- {i}단 끝 ---")
