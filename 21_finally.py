# ========================================
print(f"\n{"="*40}\n")

# else와 finally 코드

# text = "24.5"

text = "영크크"  # 비정상


temp = 0

try:
    temp = float(text)
except ValueError:
    print("ValueError문제가 발생했습니다")
except NameError:
    print("NameError문제가 발생했습니다")
finally:
    # 오류가 있건 없건 finally의 코드를 실행해 마무리
    print(temp * 2)
