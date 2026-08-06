# ========================================
print("\n" + "=" * 40 + "\n")

# 실습 open으로 파일을 열어 read, readlines로 내용을 읽기
print("실습 open으로 파일을 열어 read, readlines로 내용을 읽기")

#   ① open으로 파일을 읽기 모드 r, utf-8로 열기

#   ② read로 전체를 한 문자열로 읽어 출력

#   ③ readlines로 줄 리스트로 읽어 출력

#   ④ 두 방식의 결과 차이를 비교하고 파일을 close

# ========================================
print("\n" + "=" * 40 + "\n")


# ① open으로 파일을 읽기 모드 r, utf-8로 열기
print(" ① open으로 파일을 읽기 모드 r, utf-8로 열기\n")

f = open("data/sample.txt", "r", encoding="utf-8")

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ② read로 전체를 한 문자열로 읽어 출력
print(" ② read로 전체를 한 문자열로 읽어 출력\n")

f = open("data/sample.txt", "r", encoding="utf-8")
print(f.read())

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ③ readlines로 줄 리스트로 읽어 출력
print(" ③ readlines로 줄 리스트로 읽어 출력\n")

f = open("data/sample.txt", "r", encoding="utf-8")
print(f.readlines())

# ----------------------------------------
print("\n" + "-" * 40 + "\n")
# ④ 두 방식의 결과 차이를 비교하고 파일을 close
print(" ④ 두 방식의 결과 차이를 비교하고 파일을 close\n")

f = open("data/sample.txt", "r", encoding="utf-8")
print(f" ②\n{f.read()}")

f = open("data/sample.txt", "r", encoding="utf-8")
print(f" ③\n{f.readlines()}")


f.close
