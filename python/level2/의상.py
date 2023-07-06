"""
카테고리별로 입고 입지않고의 경우가 있기 때문에
카테고리별 +1 한 만큼의 곱이 모든 경우의수가 된다.
이 때 모든 안입었을때를 고려하여 -1 추가!
"""
def solution(clothes):
    answer = 1
    dic = {}
    
    for cloth, category in clothes :
        if category not in dic :
            dic[category] = [cloth]
        else :
            dic[category].append(cloth)
            
    for value in dic.values() :
        answer *= (len(value) + 1)
        
    answer = answer - 1
    
    return answer

# 다른 사람 풀이
# collections의 Counter, functools의 reduce를 이용한 방법
# 의상이 겹칠 수 없는 점을 이용한 방법같다
# 하지만 dictionary가 더 빠르다!
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer