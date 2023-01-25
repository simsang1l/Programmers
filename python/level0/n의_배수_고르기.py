def solution(n, numlist):
    answer = []
    
    # 배수면 나누어 떨어지겠지
    
    for i in numlist:
        if i % n == 0 :
            answer.append(i)
        
    return answer