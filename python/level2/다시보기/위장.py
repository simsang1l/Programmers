"""
하다가 막혀서 다른 사람 코드 확인
대부분 코드는 가능한 모든 경우의 수에서 한 개도 입지 않는 경우를 빼는 방법을 택했다.
"""
# 문제 풀기 위한 코드
from collections import Counter

def solution(clothes):
    # 의상의 종류별 개수 계산
    type_count = Counter([type for name, type in clothes])
    
    # 조합의 수 계산: 각 종류별 (의상 수 + 1) 을 모두 곱한 후, 아무것도 선택하지 않는 경우 1 빼기
    answer = 1
    for count in type_count.values():
        answer *= (count + 1)
    answer -= 1
    
    return answer


# 의상 종류를 보려고 만든 코드
from itertools import product
from collections import defaultdict

def solution(clothes):
    # 의상 종류별로 분류
    clothes_by_type = defaultdict(list)
    for item, type in clothes:
        clothes_by_type[type].append(item)
    
    # 각 종류별 선택 가능한 옵션 추가 (선택하지 않는 경우를 위해 None 추가)
    options_by_type = [clothes + [None] for clothes in clothes_by_type.values()]

    # 가능한 모든 조합 생성
    all_combinations = list(product(*options_by_type))

    # 적어도 하나의 의상을 선택하는 조합만 필터링
    valid_combinations = [combo for combo in all_combinations if any(combo)]

    # None을 제외한 실제 의상 이름으로 구성된 조합으로 변환
    valid_combinations = [tuple(item for item in combo if item is not None) for combo in valid_combinations]
    
    return len(valid_combinations)