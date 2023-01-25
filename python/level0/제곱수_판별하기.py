def solution(n):
    answer = 0
    
    # 제곱수
    num = 0
    i = 1
    
    while True :
        
        if i**2 == n :
            answer = 1
            break
        elif n < num:
            answer = 2
            break
            
        i += 1
        num = i**2
    
    
    return answer