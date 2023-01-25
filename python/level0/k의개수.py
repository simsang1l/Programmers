def solution(i, j, k):
    answer = 0
    
    for i in range(i, j+1):
        for val in str(i) :
            if str(k) in str(val) :
                answer += 1
            
    return answer