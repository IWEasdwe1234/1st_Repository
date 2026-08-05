# ========================================
print("\n" + "=" * 40 + "\n")

print("[표준 라이브러리]\n")
# math 표준 라이브러리
import math

print(math.sqrt(9))  #   제곱근값 3.0
print(math.ceil(4.2))  # 올림값 5
print(2**3)  #           2의 2승 = 2 * 2 * 2 = 8 math와 무관

# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됩니다
from math import sqrt, ceil

print(sqrt(9))


# ========================================
print("\n" + "=" * 40 + "\n")

print("[random 모듈]\n")

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10))  # 1~10 중 무작위 정수
print(random.choice(["정상", "경고", "위험"]))  # 셋 중 무작위

# ========================================
print("\n" + "=" * 40 + "\n")

print("[datetime 모듈]\n")

# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)  # 2026-08-05 13:18:38.978359

# ========================================
print("\n" + "=" * 40 + "\n")

print("[모듈 도움말 보기]\n")
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 봅시다!
# print(dir(math))
# help(math)


# 절대경로와 상대경로
# 절대경로의 예 : C:\Users\asd123\바탕화면\sample\code.py
# 만약 C:\Users\asd123\바탕화면\sample 폴더에 터미널을 연 상태에서
# code.py 코드를 실행하고 싶다면
# python code.py

# 위 code.py 언급부분은 사실 상대경로를 의미한다
# 그래서 절대경로로 지정해줘도 똑같이 실행될 것이다
# python C:\Users\asd123\바탕화면\sample\code.py

# 현재 경로에 있는 해당 파일이란걸 더 강조하는 상대경로 지정으로 써도 된다
# python ./code.py

# 만약 C:\Users\asd123\바탕화면\example 폴더 경로에서 위 코드를 실행하고 싶다면
# 절대경로 : python C:\Users\asd123\바탕화면\sample\code.py
# 상대경로 : python ..\sample\code.py
