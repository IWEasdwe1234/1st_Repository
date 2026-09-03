import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("data/04-03_이상의_정의_진동데이터_130_260903_Question_1.csv")

df_active = df[df["가동여부"] == 1]

plt.figure(figsize=(10, 5))
plt.plot(df_active["일자"], df_active["진동RMS"], label="진동RMS")
plt.axhline(y=4.5, color="#FC2600", linestyle="--", label="고정 임계치 (4.5 mm/s)")

plt.xlabel("일자")
plt.ylabel("진동RMS (mm/s)")
plt.title("시간에 따른 진동RMS 변화")
plt.legend()
plt.grid(True)
plt.show()
