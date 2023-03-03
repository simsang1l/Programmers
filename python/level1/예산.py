def solution(d, budget):
    answer = 0
    remain = 0
    d.sort()
    
    for i in d :
        remain += i
        if remain > budget :
            break
        
        answer += 1
    
    return answer

## 다른사람 풀이
def solution(d, budget):
    answer = 0
    d.sort()
    while budget < sum(d):
        d.pop()
        
    answer = len(d)
    
    return answer