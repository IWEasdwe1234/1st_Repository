print(f"\n{"=" * 40}\n")

# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드(r)로 utf-8 형식의 변환을 거쳐 읽기로 한다
# 가져온 정보(파인 접근 열쇠/참조값)를 f에 담는다
f = open("data/sample.txt", "r", encoding="utf-8")


# 만약 신경써서 파일 닫기(close) 해주기 귀찮다면
# with open ... as 문법을 쓰는 것도 좋다
with open("data/sample.txt", "r", encoding="utf-8") as f:
    # 앞으로 이렇게 들여쓰기 도니 코드가 끝나면
    # 파일 접근을 닫습니다(close)

    # 텍스트파일 한줄씩 문자열을 만들어 리스트만들기
    lines = f.readlines()
    print(lines)
print(type(lines).__name__, len(lines))

f.close()  # 열었다면 언젠가는 꼭 닫아줍시다
