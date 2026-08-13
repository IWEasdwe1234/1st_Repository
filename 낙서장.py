# while True:
#     print(f"\n{"살려주세요\t" * 5}\n{"\t살려주세요" * 5}")

import os
import time
import random

snow = []

while True:
    # 현재 터미널 크기 확인
    width, height = os.get_terminal_size()

    # 새로운 눈 생성
    if random.random() < 0.5:
        snow.append([random.randint(0, width - 1), 0])

    # 화면 지우기
    os.system("cls")

    # 현재 터미널 크기만큼 빈 화면 만들기
    screen = [[" " for _ in range(width)] for _ in range(height)]

    # 눈을 아래로 이동
    for s in snow:
        s[1] += 1

        # 터미널 화면 안에 있는 눈만 표시
        if s[1] < height and s[0] < width:
            screen[s[1]][s[0]] = "💧"
            # screen[s[1]][s[0]] = "🩸"
            # screen[s[1]][s[0]] = "⚡"
            # screen[s[1]][s[0]] = "🔥"
            # screen[s[1]][s[0]] = "💮"
            # screen[s[1]][s[0]] = "❄️"

    # 화면 출력
    for row in screen:
        print("".join(row))

    # 화면 아래로 떨어진 눈 제거
    snow = [s for s in snow if s[1] < height]

    # 눈이 떨어지는 속도
    time.sleep(0.08)
