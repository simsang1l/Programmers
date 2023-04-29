def solution(s):
    answer = 0
    score1, score2 = 0, 0
    
    for val in s :
        if score1 == score2 :
            answer += 1
            v = val
            
        if v == val :
            score1 += 1
        else :
            score2 += 1
            
        
    return answer