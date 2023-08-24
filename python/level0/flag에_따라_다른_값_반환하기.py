def solution(a, b, flag):
    answer = 0
    
    if flag :
        answer = a + b
    else : 
        answer = a - b
    
    return answer

# 제한 사항 적용
def solution(a, b, flag):
    answer = 0
    
    if a >= -1000 and a <= 1000 and b >= -1000 and b <= 1000:
        answer = a + b if flag else a - b
        
    
    return answer