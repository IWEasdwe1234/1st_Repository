# ========================================
print("\n" + "=" * 40 + "\n")

# 인삿말 출력 함수 간단 버전


def say_hello():
    print("안녕하세요")


say_hello()


# 인삿말 출력 함수 친근 버전
def say_hello_ned():
    print("안녕하세요, Ned")


def say_hello_tuna():
    print("안녕하세요, Tuna")


say_hello_ned()
say_hello_tuna()

# 인사할 대상이 많아진다고 위 함수들을 더 만드는건 좀 아니지않나?
# 해결책은 하나의 함수에서 저 다양성을 다 대응해주는 것
# 그것이 바로 함수의 매개변수 활용

# ========================================
print("\n" + "=" * 40 + "\n")

#


def say_hi(name):
    print(f"안녕하세요, {name}")


say_hi("Ned")
say_hi("Tuna")
say_hi("Layla")

# ========================================
print("\n" + "=" * 40 + "\n")


# 예제코드 : 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
    print(f"{name}점검을 시작합니다")


check("압축기A")
check("펌프B")


# 매개변수가 2개 이상인 예제 - 덧셈
def calc_sum(number_a, number_b):
    # number_a = 1
    # number_b = 2
    total = number_a + number_b
    print(f"{number_a}+{number_b} = {total}")


calc_sum(1, 2)


# ========================================
print("\n" + "=" * 40 + "\n")


#
# 매개변수가 2개 이상인 예제 - 장비 이름과, 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = 75.3
    print(f"{name}의 {temp}는 75.3도입니다.")


report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱하게 호출해봅시다
report(35.2, "보일러C")
# 첫번째 매개변수는 무조건 name이 되고,
# 두번째 매개변수는 무조건 temp이 되니까
# 원하지 않는 결과가 나올 수도 있다

# 매개변수가 부족하거나 더 있으면?
# report("압축기A", 75.3, "가동중") # TypeError 발생
# report("펌프B") # TypeError 발생

# ========================================
print("\n" + "=" * 40 + "\n")
