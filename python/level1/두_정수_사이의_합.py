# 가장 간단히 생각했을 때
def solution(a, b):
    answer = 0
    
    if a < b :
        for i in range(a, b+1):
            answer += i
    else : 
        for i in range(b, a+1):
            answer += i
                
    return answer

## 다른사람 코드
## 실행시간이 가장 오래걸리는거 기준 2배는 빠른듯

def solution(a, b):
    answer = sum(range(min(a,b), max(a,b) + 1))
    
    return answer