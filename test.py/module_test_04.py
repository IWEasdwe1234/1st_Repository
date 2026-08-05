# ========================================
print("\n" + "=" * 40 + "\n")

print("실습 4.os로 파일 존재 확인하기")
# 실습 4. os로 파일 존재 확인하기

# 목표
# os.path.join으로 경로를 만들고 exists로 파일 존재를 판단하기

# 단계
#   ① os를 import

#   ② path.join으로 폴더와 파일 이름을 이어 경로를 만들기

#   ③ path.exists로 그 경로가 있는지 참·거짓 확인

#   ④ if로 있으면·없으면 다른 메시지 출력

# ========================================
print("\n" + "=" * 40 + "\n")

# ① os를 import
print("① os를 import\n")

import os

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ② path.join으로 폴더와 파일 이름을 이어 경로를 만들기
print("② path.join으로 폴더와 파일 이름을 이어 경로를 만들기\n")

path = os.path.join("data", "08_press.csv")

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ③ path.exists로 그 경로가 있는지 참·거짓 확인
print("③ path.exists로 그 경로가 있는지 참·거짓 확인\n")

print(os.path.exists(path))  # False

# ----------------------------------------
print("\n" + "-" * 40 + "\n")

# ④ if로 있으면·없으면 다른 메시지 출력
print("④ if로 있으면·없으면 다른 메시지 출력\n")

if os.path.exists(path):
    print(f"파일 있음: {path}")
else:
    print(f"파일 없음: {path}")

# 파일 없음: data\08_press.csv
