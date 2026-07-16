# 산술 연산자
# + _ * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5)  # 8
print(10 - 4)  # 6
print(4 * 5)  # 20
print(20 / 4)  # 5.0 (나눗셈 결과는 항상 float)
print(7 // 3)  # 2 (나눗셈 결과의 몫)
# 7개의 음료수를 3봉투에 나눠 담으면, 2봉투와 1개의 음료수가 남음
print(7 % 3)  # 1 (나눗셈 결과의 나머지)
print(2**5)  # 32 (2의 5제곱)

# =================================
# 연산 우선순위와 우선순위 지정

# **(거듭제곱) > *(곱하기) /(나누기) //(몫) %(나머지) > +(더하기) -(빼기)

print(2 + 8 * 3)  # 8*3 연산 후 그 결과를 2와 더함
print((2 + 8) * 3)  # 괄호 안의 연산을 먼저 한 뒤 곱하기 계산

# =================================
# 복합연산자

result = 3 * 5
print(result)  # 15

# +=: 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -=: 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# *=: 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /=: 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10  # 25
print(result)
result -= 5  # 20
print(result)
result *= 3  # 60
print(result)
result /= 2  # 30.0
print(result)

# =============================
# 문자열 연산
print("안녕" + "하세요")  # 안녕하세요

# 만약 "안녕"과 "하세요" 사이에 공백을 1개 넣고 싶다면
# 방법 1) , 사용
print("안녕", "하세요")
# 방법 2) 안녕 뒤에 공백 추가
print("안녕 " + "하세요")
# 방법 3) 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5)  # 안녕안녕안녕안녕안녕

# 문자열에 연산자를 사용할 경우 모두 이어져서 나옴

# ==================================
print("=== 비교연산자 ===")

# <(미만), >(초과), <=(이하), >=(이상), ==(같다), ~=(다르다)
# 비교 결과는 무조건 True or False (bool)

print(7 < 16)  # True
print(7 > 16)  # False
print(7 <= 7)  # True
print(7 >= 7)  # True
print(7 == 7)  # True
print(7 != 7)  # False

# 비교연산자는 문자열 비교도 가능
print("hello" == "hello")  # True
print("정상" == "정상")  # True

# 비교연산자를 사용해 문자열을 비교할 때 주의사항

# 1. 대소문자 구분
print("hello" == "Hello")  # False

# 2. 공백이 있어도 다르다고 판단
print("정상" == "정상 ")  # False

# 부정연산자 != (not)
# 두 값이 동일한데 !로 인해서 값이 반대로 출력됨
print("hello" != "hello")  # False
print("hello" != "hello ")  # True
print("hello" != "Hello")  # True

# 변수에 문자열을 할당하고, 변수로 문자열 비교
hello = "hi"
print(hello == "hi")
# 위 비교에서 hello는 따옴표로 감싸지지 않아서 "변수"로 취급
# 만약 hello를 "hello"와 같이 따옴표로 감싸면
# string으로 인식해서 변수 취급을 하지 않음
# ex) "hello"와 "hi"를 비교하는 것

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2)  # False
# print(num1 >= "num2")  # TypeError 발생
# TypeError: '>=' not supported between instances of 'int' and 'str'

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
print("=== 변수 hello(안녕)와 변수 hi(안녕)비교")
# hello = hi
# print(hello == hi) # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취도됨
# 그런데 우리는 변수를 선언한 적이없기 떄문에 에러

# 질문 1) 해결방법
hi = "안녕"
hello = hi  # print(hello) > 안녕
print(hello)

# ========================================

# and / or / not - 논리연산자
# and: 둘 다 True 여야 True를 반환
print(5 == 5 and 7 == 7)  # True + True = True
print(5 == 7 and 7 == 7)  # False + True = False
# 첫 번째 조건이 False라면 뒤에 조건은 확인 안함 (가능하면 False가 나올 값을 앞으로 -> 계산 작업 단축)
print(5 == 5 and 7 != 7)  # True + False = False
# 위 코드는 가능하다면 7 != 7 and 5 == 5 순서로 작성

# or: 하나라도 True라면 True 반환
print(5 == 5 or 7 == 7)  # True + True = True
print(5 == 7 or 7 == 7)  # False + True = True
print(5 == 5 or 7 != 7)  # True + False = False
# 첫 번째 조건이 True라면 뒤에 조건은 확인 안함
print(5 == 5 or 7 != 7)  # True + False = True

# not: 값을 반대로 뒤집음
print(not True)  # False
print(not 5 == 5)  # False
# 5 == 5를 연산하여 True를 반환
# not True로 동작해서 True를 뒤집어 False 반환
# 반환받은 False라는 값을 print가 터미널로 출력

# =========================
print("=== 실습3 비교연산출력 ===")
# 목표 : 비교 연산자 6종겨결ㄱ과(True/Fals)직접 확인
# 1. 같다(==), 다르다(!=)
# 2. 크다(>), 작다(<)
# 3. 이상(>=), 이하(<=)
print(1 == 1)  # True
print(2 != 1)  # True
print(3 > 1)  # True
print(4 < 1)  # False
print(5 >= 1)  # False
print(6 <= 1)  # False

# =========================
print("=== 실습4 정상범위 다중센서 판정 실전 ===")
# 목표: 값이 정상범위 안인지, 여러 센서가 모두 정상인지 판정
# 단계 :
# - 온도 변수에 85할당 -> 60이상, 90이하인지 비교하여 새로 생성한 변수에 저장
# - 압력 변수에 5할당 -> 3이상, 7이하인지 비교하여 결과 새로 생성한 변수에 저장
temp = 85
pressure = 5
print(temp >= 60 and temp <= 90)  # True
print(pressure >= 3 and pressure <= 7)  # True
print((temp >= 60 and temp <= 90) and (pressure >= 3 and pressure <= 7))  # True

# =========================
print("=== 실습5 복합 할당으로 재고 추적 ===")
# 목표: 복합 할당 연산자(+=,-=)로 재고 수량을 갱신
# 단계 :
# 1. 재고 100
# 2. 입고 += 50
# 3. 출고 -+30, 반품 +=5
stock = 100
stock += 50
print(stock)  # 150(입고)
stock -= 30
print(stock)  # 120(출고)
stock += 5
print(stock)  # 125(반품)

# =========================
print("=== 실습6 설비 지표 계산 실전 ===")
# 목표: 생산 가동 데이터로 불량률 가동률(%)을 계산
# 단계 :
# 1. 전체 500, 불량 23일 때 불량률 계산
# 2. 가동 21h, 전체 24일 때 가동률
total = 500
defect = 23
print(defect / total * 100)  # 4.6 (불량률 %)
run_h = 21
all_h = 24
print(run_h / all_h * 100)  # 87.5 (가동률 %)

# =========================
print("=== 실습7 시간 변환 상자 포장 도전 ===")
# 목표: 총 가동 분(500분)을 시:분으로 변환하여 출력
minutes = 500
print(minutes // 60)  # 8 (시간)
print(minutes % 60)  # 20 (분)
