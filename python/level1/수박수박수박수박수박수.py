def solution(n):
    answer = ''
    watermelon = '수박'
    
    for i in range(n):
        if i % 2 == 0 :
            answer += watermelon[0]
        else : 
            answer += watermelon[1]
    
    return answer