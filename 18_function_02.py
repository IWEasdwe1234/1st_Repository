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
