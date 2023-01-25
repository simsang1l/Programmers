def solution(n):
    answer = 0
    curse_num = list()
    
    for i in range(n):
        answer += 1
        
        while answer % 3 == 0 or '3' in str(answer) :
            answer += 1
        
    return answer