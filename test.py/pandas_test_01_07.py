# 실습 7. 통계량 문장으로 묘사
print("\n실습 7. 통계량 문장으로 묘사\n")

import pandas as pd

# 실습 과제
# 설비 센서 데이터의 한 열 묘사
# 온도·진동·전류 중 하나 골라 문장으로


# describe 통계를 자기 말로 풀어 설명

# 설비 센서 데이터의 "한 열(1 colum)"을 묘사

df = pd.read_csv("data/12_metro_compressor.csv")
print("\n[df.info()] 실행\n")
df.info()

print(f"\n{"-"*20}\n")

# 오일온도 컬럼만 떼서 describe 통계 보기
print('\ndf["오일온도"].info() 실행\n')
df["오일온도"].info()

print(f"\n{"-"*20}\n")

print('\ndf["오일온도"].describe()) 출력\n')
print(df["오일온도"].describe())

print(f"\n{"-"*20}\n")

# print('\n["df오일온도"] 출력')
# print(df["오일온도"])
