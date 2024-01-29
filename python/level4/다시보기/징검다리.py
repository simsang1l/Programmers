# 다시 보기

# 예상은 했지만 시간초과된 case가 많다
from itertools import combinations

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    min_lst = []
    
    rock_lst = list(combinations(rocks, len(rocks) - n))
    print(rock_lst)
    for rock in rock_lst:
        rock = list(rock)
        rock.insert(0, 0)
        rock.insert(len(rocks)+1, distance)
        d = []

        for i in range(1, len(rock)):
            d.append(rock[i] - rock[i-1])

        min_lst.append(min(d))        
    answer = max(min_lst)
    
    return answer