# # tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 python이 튜플로 인식을 함
# 짝찌어진 값을 하나로 묶을 때 사용 가능한 자료형

# == 튜플 만들기 ==
print("\n== 튜플 만들기 ==")

# 예시 1)
print("\n괄호 있고, 끝에 쉼표 없음")
sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 예시 2)
print("\n괄호 없고, 끝에 쉼표 없음")
sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 예시 3)
print("\n괄호 있고, 끝에 쉼표 있음")
sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 예시 4)
print("\n괄호 없고, 끝에 쉼표 없음")
sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

# 예시 5)
print("\n괄호 있고, 끝에 쉼표 있음")
sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 예시 6)
print("\n괄호 있고, 끝에 쉼표 없고, 값도 안담김")
sensor = ()  # 괄호 있고, 끝에 쉼표 없고, 값도 안담김
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 튜플
# 요소 1개: 쉼표 여부
# 요소0개(빈 튜플): () 빈 괄호

# 튜플에서 많이 헷갈려하는 부분
# (1): int
# (1,): tuple

# (1, 2, 3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# (1, 2, 3) -> 튜플 맞음


# 튜플의 인덱스
print("\n튜플의 인덱스")

sensor = ["모터온도", 78]
print(sensor[0])

# 튜플의 슬라이싱
print("\n튜플의 슬라이싱")

s = (
    "a",
    "b",
    "c",
    "d",
    "e",
)
print(s[1:4])
# 슬라이싱한 결과는 소괄호에 감싸져 있음
# 튜플은 슬라이싱해도 결과가 튜플
print(type(s[1:4]))  # <class 'tuple'>

# 튜플 언패킹
print("\n튜플의 언패킹")
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언
a, b, c = "a", "b", "c"
print(a)  # 문자열 a
print(b)  # 문자열 b
print(c)  # 문자열 c

unpacking = (
    1,  # 변수 one
    2,  # 변수 two
    3,  # 변수 three
)

# unpacking = one, two, three
# one two three라는 알 수 없는 변수를
# unpaking 변수에 할당하겠다는 의미
# 동작 X

one, two, three = unpacking
# unpacking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에
# 풀어서 담는다는 뜻
print("one:", one)
print("two:", two)
print("three:", three)


# print("one:", one)
# print("two:", two)
# print("three:", three)
# print("four:", four)
# one, two, three, four = unpacking
# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함
print("\n")

# 리스트 언패킹이 가능할까?
one, two, three, four = [11, 22, 33, 44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)
# 가능!


# ==============================
print("\n=======================\n")

tup = (
    "normal",
    "normal",
    "warning",
    "normal",
    "warning",
)

# 튜플의 길이
print(len(tup))  # 5

# 특정 값의 갯수 세기
print(tup.count("warning"))  # 2
print(tup.count("Warning"))  # 0

# 특정 값이 처음 나온 인덱스 찾기
print(tup.index("warning"))  # 2
# 찾고자 하는 값이 없으면 Error 발생
# print(tup.index("Warning"))  # ValueError: tuple.index(x): x not in tuple


# ==============================
print("\n=======================\n")

# 튜플 리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서
# 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

print("\n- 튜플 리스트 -\n")

print('\nhour_13 = [("모터온도", 77),("모터진동", 0.2),("모터압력", 91),]\n')

hour_13 = [
    ("모터온도", 77),
    ("모터진동", 0.2),
    ("모터압력", 91),
]

now = 0

for name, value in hour_13:
    now += 1
    print(now, "번째 반복")
    print("name", name, "value", value)


print("\n")
print("\n- 설비 온도 -")

temps_13 = [
    ("qox_001", 81),
    ("qox_001", 88),
    ("qox_001", 95),
    ("qox_001", 89),
]

Warning = 90

for name, temp in temps_13:
    if temp >= Warning:
        print(name, "설비 온도 이상")

print("\n")
# 리스트 안의 튜플 값 갯수가 늘어나면
# for문에서 변수를 여러개 작성하면 됨

tup_list = [
    ("일,", "one", 1, "1"),
    ("이,", "two", 2, "2"),
]

# for문에서도 언패킹할 때는 무조건 튜플의 값 갯수와
# for문의 변수 갯수 통일
# 통일하지 않을 경우 Error 발생
for kor_str, eng_str, num, num_str in tup_list:
    print("kor_str", kor_str, "eng_str", eng_str, "num", num, "num_str", num_str)
