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
