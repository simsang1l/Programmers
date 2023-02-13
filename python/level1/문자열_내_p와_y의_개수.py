def solution(s):
    answer = True
    p = 0
    y = 0
    
    for i in s.lower():
        if i == 'p' :
            p += 1
        elif i == 'y':
            y += 1
            

    if p == 0 and y == 0:
        answer = True
    elif p == y :
        answer = True
    else : 
        answer = False
        
        
    return answer


## 다른사람풀이
