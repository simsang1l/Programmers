def solution(s):
    answer = True
    p = 0
    y = 0
    
    for i in s.lower():
        if i == 'p' :
            p += 1
        elif i == 'y':
            y += 1
            

    if p == y :
        answer = True
    else : 
        answer = False
        
        
    return answer


## 다른 사람 풀이 
def solution(s):
    return s.lower().count('p') == s.lower().count('y')