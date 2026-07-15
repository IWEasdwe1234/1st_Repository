# int - 정수형
# 소수점 없이 딱 떨어지는 수

count = 3
age = 20
tall = 173

# 0과 음수도 정수에 포함됨
zero = 0
temp = -30

# ==========================

# float - 실수
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수이지만 소수점이 있다면 무조건 float

tired = 99, 99999
height = 17.2

# ==========================

# str - 문자열
# 따옴표에 감싸져있는 모든 값

hello = "안녕하세요~!"
emoji = "♥️"
empty = ""  # 따옴표만 있고 아무것도 작성되지 않아도 str
fake_num = "12345"
fake_num2 = "5.0"
# 따옴표가 ""와 '' 둘 다 사용할 수 있는 이유는
# 문자열 안에 따옴표가 필요한 경우가 있기 때문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 가장 바깥에 감싸줘야 함
illit = "It's me"

# ==========================

# bool - 불리언형
# True 또는 False만
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
np = False

# 비교할 경우 bool로 출력
print(110 < 5)  # False
print(5 == 5)  # True

# ==========================
print("=== type() ===")  # 터미널에서 출력 결과 확인할 때 가독성을 위한 코드
# type() - 자료형 확인
# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌


type(5)  # 터미널에서 확인 불가 > print하지 않았기 떄문

print(type(5))  # <class 'int'>
print(type("센서"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(3 > 2))  # <class 'bool'>
# 1. print 함수의 내부를 확인
# 2. print 함수에 또 함수가 있는 것을 확인하고 해당 type 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3 > 2의 연산 결과는 True이기 떄문에 type(True)로 바뀜
# 5. type(True)dml rufrhkdls <class 'bool'>이 print로 인해 터미널에 출력

print(3, type(3))  # 3, <class 'int'>

num = 123
fake_num = "123"
str = "문자열"
ok = True

# 값과 결과를 동시에 확인
print(num, type(num))  # 123 <class 'int'>

# 내가 터미널에서 출력된 결과 중에서
# type()을 사용해서 출력된 자료형을 쉽게 확인할 수 있는 방법
print("num >>>", type(num))  # num >>> ,class 'int'>
print("num :", type(num))  # num : ,class 'int'>

# ==========================

print("=== 자료형마다 동작이 다른 것 확인하기 ===")

print(3 + 5)  # 8 (int) > 숫자끼리 더하기는 계산
print("3" + "5")  # 35 (str) > str끼리 더하기는 이어 붙이기
print("안녕하" + "세요")  # 안녕하세요

# ==========================
print("=== 자주 하는 실수 ===")

print(0.1 + 0.8)  # 0.9
# 위 상황에서는 출력되지만
#  가끔 컴퓨터 내부 연산 과정에서 아주 작은 오차가 발생하는 경우도 있음

# 작은 오차 해결법
# round() 사용해서 반올림
print(round(0.1 + 0.8, 2))  # 소수 둘째 자리를 반올림해서 0.9 출력

# str과 int/float은 덧셈 불가
# print("123" + 456)  # TypeError 발생

print(10 / 2)  # 5.0 (나눗셈은 결과가 딱 떨어져도 무조건 float)
print(type(10 / 2))  # <class 'float>

# ====================================
print("=== 실습1 여러 자료형 변수 ===")
# 네 가지 자료형 변수를 한 줄씩 그대로 입력하고, 매 줄 실행하며 확인함
# 1단계 정수(int) count 변수 만들기
count = 5 + 7
print(count)  # 12
# 2단계 실수(float) temp 변수 만들기
temp = 15 / 3
print(temp)  # 5.0
# 3단계 문자열(str) name 변수 만들기
name = "문자열"
print(name)  # 문자열
# 4단계 불린(bool) is_ok 변수 만들기
is_ok = True  # bool
# 5단계 생성한 변수 모두 출력
print(count, temp, name, is_ok)  # 12 5.0 문자열 True

# ====================================
print("=== 실습2 type()으로 자료형 확인하기 ===")
# 실습 1에서 만든 변수들의 종류를 type()으로 하나씩 확인함
# 1단계 count 의 자료형 확인
print(type(count))  # <class 'int'>
# 2단계 temp 의 자료형 확인
print(type(temp))  # <class 'float'>
# 3단계 name 의 자료형 확인
print(type(name))  # <class 'str'>
# 4단계 is_ok 의 자료형 확인
print(type(is_ok))  # <class 'bool'>

# ====================================
print("=== 실습3 자료형 맞히기 퀴즈 ===")
# 각 값의 자료형을 종이에 먼저 적어 예측한 뒤, type()으로 실행해 채점함
# 1단계 100 의 자료형 예측하여 주석으로 작성하기
print(type(100))  # <class 'int'>
# 2단계 100.0 의 자료형 예측하여 주석으로 작성하기
print(type(100.0))  # <class 'float'>
# 3단계 "100"의 예측하여 주석으로 작성하기
print(type("100"))  # <class 'str'>
# 4단계 type()으로 셋 다 채점하기

# ====================================
print("=== 실습4 문자열 숫자와 숫자 비교하기 ===")
# 같은 + 기호라도 숫자와 글자에서 결과가 다름을 직접 실행해 비교함
# 1단계 진짜 숫자끼리 더하기
print(4 + 16)  # 20
# 2단계 글자 숫자끼리 더하기
print("4" + "16")  # 416
# 3단계 두 자리 숫자 더하기
print("24" + "44")  # 2444
# 4단계 두 결과 차이 확인하기

# ====================================
print("=== 실습5 bool 값 만들어 확인하기 ===")
# 비교의 결과가 참/거짓(bool)임을 직접 실행해 확인함
# 1단계 3 이 2보다 큰지 주석으로 작성 후 결과 출력해보기
print(3 > 2)  # True
# 2단계 5 와 5 가 같은지 결과 출력해보기
print(5 == 5)  # True
# 3단계 값을 비교하는 type의 자료형 출력하기
print(type(1 > 5))  # <class 'bool'>

# ====================================
print("=== 실습6 변수의 자료형 변경하기 ===")
# 값에 소수점 따옴표를 더해, 자료형이 어떻게 바뀌는지 type()으로 확인함
# 1단계 정수 변수를 선언하고, 자료형 출력하기
count = 4
print(count, type(count))
# 2단계 정수를 실수로 값을 재할당하여 자료형 출력하기
count = 3.0
print(count, type(count))
# 3단계 숫자를 글자로 값을 재할당하여 자료형 출력하기
count = "3"
print(count, type(count))

# ====================================
print("=== 실습7 직접 자료형 표현하기 ===")
# 변수 이름에 맞는 자료형을 골라 값을 직접할당하기
# 1단계 device_temp 변수 선언하기
device_temp = 25.5  # float
# 2단계 check_count 변수 선언하기
check_count = 12  # int
# 3단계 device_name 변수 선언하기
device_name = "펌프A"  # str
# 4단계 is_normal 변수 선언하기
is_normal = True  # bool
