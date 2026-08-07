# ========================================
print(f"\n{"="*40}\n")

# 실습 1. finally로 파일 안전하게 닫기
print("실습 1. finally로 파일 안전하게 닫기\n")

# try-finally로 오류가 나도 파일을 반드시 닫기

# ① try 블록에서 파일을 열어 처리

# ② 처리 도중 오류가 날 수 있음을 가정

# ③ finally 블록에 close를 넣어 오류 여부와 상관없이 닫기

# ④ 일부러 오류를 내도 finally가 실행되는지 확인

# ========================================
print(f"\n{"="*40}\n")

try:
    f = open("data/sample.txt", "r", encoding="utf-8")
    print(f.read())

    print(int(오류))
except NameError:
    print("\n🚨정수가 아닙니다🚨\n")
finally:
    f.close()
    print("파일을 닫았습니다\n")
