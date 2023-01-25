def solution(num, k):
    answer = 0
    
    if str(k) in str(num) :    
        for idx, value in enumerate(str(num)) :
            if int(value) == k:
                answer = idx + 1
                break
    else :
        answer = -1
        
            
    return answer