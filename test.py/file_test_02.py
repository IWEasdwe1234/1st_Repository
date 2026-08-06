# ========================================
print(f"\n{"=" * 40}\n")

# 실습2. open으로 파일을 열어 read, readlines로 내용을 읽기
print("실습2. open으로 파일을 열어 read, readlines로 내용을 읽기")

#   ① with open으로 파일을 쓰기 모드 w, utf-8로 열기

#   ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)

#   ③ with 블록이 끝나면 파일이 자동으로 닫힘

#   ④ r 모드로 다시 열어 쓴 내용을 확인


# ========================================
print(f"\n{"=" * 40}\n")


# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기
print(" ① with open으로 파일을 쓰기 모드 w, utf-8로 열기\n")

with open("hello.txt", "w", encoding="utf-8") as f:

    # ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
    f.write("점심시간\n")
    f.write("\t11시 40분부터\n")

    # ③ with 블록이 끝나면 파일이 자동으로 닫힘
    # 정상적으로 닫힘

# # ④ r 모드로 다시 열어 쓴 내용을 확인
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())
