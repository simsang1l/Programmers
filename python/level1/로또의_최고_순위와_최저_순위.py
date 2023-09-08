def grade(score):
    if score == 6 :
        return 1
    elif score == 5 :
        return 2
    elif score == 4 :
        return 3
    elif score == 3 :
        return 4
    elif score == 2 :
        return 5
    else :
        return 6
    
def solution(lottos, win_nums):
    
    consensus = 0
    for num in lottos:
        if num in win_nums:
            consensus += 1
    zero_cnt = lottos.count(0)
    
    answer = [grade(zero_cnt + consensus), grade(consensus)]
    return answer

# 다른 사람 풀이 
## 두 점수 리스트에 대한 교집합을 이용한 풀이!
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

## 직관적인 풀이
def solution(lottos, win_nums):
    zero = lottos.count(0)
    a= [x for x in lottos if x in win_nums]
    max = zero+len(a)
    min = len(a)

    max = 7- max if max >=1 else 6
    min = 7- min if min >=1 else 6
    return [max,min]