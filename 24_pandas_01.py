# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가상환경 활성화
# source .venv/Scripts/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 기능, 예 pip install pandas)

# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate

import pandas
import os

filepath = os.path.join("data", "12_metro_small.csv")

try:
    df_metro_small = pd.read_csv(filepath, encoding="utf-8", sep=";", nrows=5)
    print(df_metro_small.shape)  # (30, 7)

    print(df_metro_small.head(10))
except FileNotFoundError:
    print(f"\n파일이 없습니다 : {filepath}\n")
