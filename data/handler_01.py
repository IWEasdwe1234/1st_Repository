# 트레이스백으로 에러 읽기

# ValueError: 글자를 숫자로 변환 요구 - 당연히 실패
# temp = int("스물")

# Traceback (most recent call last):
#   File "c:\Users\PC2510\Desktop\1st_Repository\data\handler_01.py", line 4, in <module>
#     temp = int("스물")
#            ~~~^^^^^^^^
# ValueError: invalid literal for int() with base 10: '스물'

# 정상화
temp = int("20")
print(temp)

# ========================================
print(f"\n{"="*40}\n")

# result = 10 / 0
# Traceback (most recent call last):
#   File "c:\Users\PC2510\Desktop\1st_Repository\data\handler_01.py", line 19, in <module>
#     result = 10 / 0
#              ~~~^~~
# ZeroDivisionError: division by zero

# 정상화
result = 10 / 3

# ========================================
print(f"\n{"="*40}\n")

# hello()
# Traceback (most recent call last):
#   File "c:\Users\PC2510\Desktop\1st_Repository\data\handler_01.py", line 31, in <module>
#     hello()
#     ^^^^^
# NameError: name 'hello' is not defined. Did you mean: 'help'?

# 정상화
print("hello")
