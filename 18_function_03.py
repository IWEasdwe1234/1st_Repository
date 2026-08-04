# 07_03 함수 설계와 활용


# ========================================
print("\n" + "=" * 40 + "\n")

print("기본값 인자\n")


# 기본값 인자
# name과 value는 호출할 때 꼭 매개변수를 지정해줘야하지만
# unit은 지정/언급 안해주면
def report(name, value, unit="도(℃)"):
    print(f"{name} : {value}{unit}")


report("압축기A", 75.3, "도(℃)")
report("압축기A", 75.3)
report("압축기A", 75.3, "도(℉)")


# ========================================
print("\n" + "=" * 40 + "\n")

print("기본값 덮어쓰기\n")
# 기본값 덮어쓰기
# 결과가 boolean 타입을 return하는 함수는
# 이름이 보통 "is"로 시작한다.


def is_over_limit(value, limit=90):
    if value > limit:
        # 위험 맞음
        return True

    # 그 밖에는 위험 아님
    return False


print(f"위험한가요? {is_over_limit(95)}")
print(f"위험한가요? {is_over_limit(105)}")
# 어쩌다 다른 기준이 필요할 때만
# 기준을 함꼐 전달해주면 된다
print(f"위험한가요? {is_over_limit(85, limit=80)}")
