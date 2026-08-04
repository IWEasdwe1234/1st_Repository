#
#  어제처럼 주변 3~4인과 함께 코드를 만드세여
# 가봤거나, 가보고싶은 여행지 정보를 모아봅시다 (최소 5개 이상)
# 함수를 호출하면 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다! 000 나라의 수도 000 입니다!" 출력

import random

travel_destinations = [
    {"국가": "대한민국", "수도": "서울"},
    {"국가": "일본", "수도": "도쿄"},
    {"국가": "러시아", "수도": "모스크바"},
    {"국가": "프랑스", "수도": "파리"},
    {"국가": "미국", "수도": "워싱턴 D.C."},
]


def recommend_travel():
    selected_place = random.choice(travel_destinations)

    country = selected_place["국가"]
    capital = selected_place["수도"]

    print(f"환영합니다! {country} 나라의 수도 {capital} 입니다!")


print("\n=== 여행지 랜덤 추천 ===")
recommend_travel()
