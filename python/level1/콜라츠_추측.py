# 문제 설명 그대로 구현하고자 함
# 최대 500번 수행

def solution(num):
    answer = 0
    
    while answer <= 500:
        if num % 2 == 0 :
            num = num//2
        elif num == 1 :
            break
        else :
            num = num * 3 + 1
            
        answer += 1
            
    if answer > 500 : 
        answer = -1
    
    return answer
