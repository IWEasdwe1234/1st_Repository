# 실습 5. info로 데이터 건강검진
print("\n실습 5. info로 데이터 건강검진\n")

import pandas as pd

# 실습 과제
# metro_digital_sample.csv
# 결측 많음

df = pd.read_csv("data/12_metro_digital.csv")

print("[info() 실행]")
df.info()
