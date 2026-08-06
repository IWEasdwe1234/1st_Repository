print(f"\n{"="*40}\n")

temp = -1

try:
    temp = int("스물")
except:
    print("해봤는데 안되네요")
    temp = 0  # 문제가 있어도 앞으로 잘 진행되도록 대안/추가 처리 필요

print(temp)

print(f"\n{"="*40}\n")

# 실습2. try-except로 오류 넘기기

origin = input("온도 입력 : ")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except ValueError:
    # ValueError인 상황이었다면 여기로 예외처리
    print("숫자 아니면 왜 저를 부르셨어요?")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")
