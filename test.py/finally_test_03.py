# ========================================
print(f"\n{"="*40}\n")

# 실습 3. 여러 파일 묶어 처리하기
print("실습 3. 여러 파일 묶어 처리하기\n")

# - 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# - for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됩니다

# file_names = ["08_press.cvs", "09_ict.csv", "09_ict_dirty.csv"]

# ========================================

file_names = [
    "08_press.csv",
    "09_ict.csv",
    "09_ict_dirty.csv",
    "10_dirty_dirty2",
    "sample.txt",
]

for file_name in file_names:
    try:
        file = open(file_name, "r", encoding="utf-8")

        print(file_name, "파일 열기 성공")

        file.close()

    except FileNotFoundError:
        print(file_name, "파일을 찾을 수 없습니다.")
