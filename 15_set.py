# set
# 자동 중복 제거
# 순서가 없음
# 형태는 중괄호로 감쌈

# 빈 set 만들기
print("\n- 빈 set 만들기 -")

empty_list = []
print(type(empty_list))  # <class 'list'>
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>

empty_set = {}
print(type(empty_set))  # <class 'dict'>
# 빈 중괄호는 딕셔너리라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장함수를 사용
real_empty_set = set()
print(type(real_empty_set))  # <class 'set'>

# 값을 포함한 셋 만들기
logs = ["S01", "S02", "S01", "S03", "S01"]

# 리스트를 {}에 감쌀 경우
# TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# unique = {logs}

# 복수의 값을 중괄호에 감싸 작성
print("\n- 복수의 값을 중괄호에 감싸 작성 -")
unique = {"S01", "S02", "S01", "S03", "S01"}
print(type(unique))  # <class 'set'>
print(unique)  # {'S02', 'S01', 'S03'}

# set() 사용
print("\n- set()사용 -")
unique = set(logs)
print(type(unique))  # <class 'set'>
print(unique)  # {'S02', 'S01', 'S03'}
# unique 셋에는 기존 중복되었던 S01이 한 번만 들어감
# 지금은 길이가 짧아서 순서대로 정렬된 것처럼 보이지만
# 셋은 순서가 없는 값의 묶음
# print(unique[0])  #TypeError: 'set' object is not subscriptable
# set에서 인덱스 사용 시 Error 발생

# set에 바로 여러 값을 작성
print("\n- set에 바로 여러 값을 작성 -")
unique = set(["S01", "S02", "S01", "S03", "S01"])
print(type(unique))  # <class 'set'>
print(unique)  # {'S02', 'S01', 'S03'}

# set을 사용해서
# 리스트에 들어있는 유니크한 값의 종류 수를 알 수 있음
print("\n- set()사용헤서 값의 종류 수를 알 수 있음 -")
print(len(unique))  # 3

# =======================
print("\n=================")

# 셋에 값 추가하기
# 셋.add(추가할 값)
print("\n- 셋.add(추가할 값) -")
# 이미 있는 값을 추가할 경우 무시

alerts = {"S01", "S02"}

# 경고 상태인 S03이 추가될 경우
# .add()를 사용해서 추가
alerts.add("S03")
print(alerts)  # {'S02', 'S03', 'S01'}

# S01에서 또 경고가 발생
print("\n- S01에서 또 경고가 발생(S01) -")
# 이미 S01은 경고가 발생한 적이 있고
# alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관 없이
# 이럴 때 set을 쓰면 변리함
alerts.add("S01")
print(alerts)  # {'S02', 'S03', 'S01'}
# S01이라는 값을 또 넣어도 무시하고 한 번만 저장
# 그래서 독립적인 값을 저장하기에는 아주 편리함


# =======================
print("\n=================")

# set에 특정 값 포함 여부 확인
# ["S01", "S02", "S01", "S03", "S01"]
# {"S01", "S02", "S03"}
# 리스트와 셋을 비교해보면
# set이 길이가 짧은 (중복을 제거하기 떄문에)
# set은 인덱스가 없음
# 순회 속도가 리스트보다 훨씬 빠름

print('\n- "S01" in alerts -')
print("S01" in alerts)  # True
# 이렇게 출력하기보단 조건문을 활용해서
# 포함 여부 확인 후 특정 동작을 실행시킴
print("\n- 조건문 활용 -")
if "S01" in alerts:
    print("S01 정비 필요")


# 질문) set을 정렬한다면?
print("\n질문) set을 정렬한다면?")

sorted_alerts = sorted(alerts)
print(sorted_alerts)  # ['S01', 'S02', 'S03']
print(type(sorted_alerts))  # <class 'list'>
# 정렬을 한다는 것은 순서가 필수불가결하게 따라오는 개념
# set을 정렬하면 리스트로 형이 변환됨


# 실습4. 셋으로 중복 센서 제거하기
print("\n실습4. 셋으로 중복 센서 제거하기")

logs = ["WQR_01", "WQR_01", "WQR_01", "WQR_01", "WQR_06", "WQR_06", "WQR_03", "WQR_05"]
unique = set(logs)

print(sorted(unique))
print("종류 수", len(unique))


# =======================
print("\n=================")

# 집합 연산
print("\n-- 집합 연산 --")
hour_14 = {"WQR_01", "WQR_06", "WQR_07", "WQR_02"}
hour_15 = {"WQR_01", "WQR_07", "WQR_03", "WQR_09", "WQR_11"}

# 합집합
print("\n- 합집합 -")

print("\n- .union()사용 -")

print(hour_14.union(hour_15))
print(hour_15.union(hour_14))  # 두 코드는 동일한 동작
# {'WQR_01', 'WQR_02', 'WQR_03', 'WQR_06', 'WQR_07', 'WQR_09'}
# 짧게 정리: 1, 2, 3, 6, 7, 9, 11

print("\n- hour_14 출력 -")
print(hour_14)  # .union은 원본 셋에 변화 X

print("\n- | 기호 사용 -")

print(hour_14 | hour_15)  # 연산자를 활용해 짧게 작성 가능

# 교집합
print("\n- 교집합 -")
# union이랑 동일하게 두 코드는 똑같은 결과를 출력
# 앞뒤 순서가 결과에 영향을 미치지 않음

print(hour_14.intersection(hour_15))
print(hour_15.intersection(hour_14))

# & 연산자 사용 교집합
print("\n- & 연산자 사용 -")
print(hour_14 & (hour_15))

# 3개의 print문은 공통으로 {'WQR_01', 'WQR_07'} 출력

# 차집합
print("\n- 차집합 -")
# 순서에 따라 결과가 다름
# 앞에 작성된 셋에서
# difference의 인자로 전달된 셋에 있는 값들을
# 제외한 결과를 출력

print(hour_14.difference(hour_15))  # {'WQR_02', 'WQR_06'}
print(hour_15.difference(hour_14))  # {'WQR_03', 'WQR_09'}

# - 연산자 사용 차집합
print("\n- - 연산자 사용 차집합 -")
print(hour_14 - (hour_15))  # {'WQR_02', 'WQR_06'}
print(hour_15 - (hour_14))  # {'WQR_03', 'WQR_09'}
# 차집합은 순서에 따라 결과가 다른 것을 유의
# 14 - 15와 51 - 14는 다름
# 빼는 방향에 따라 결과가 달라짐
