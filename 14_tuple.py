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
