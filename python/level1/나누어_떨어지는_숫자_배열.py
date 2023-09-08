def solution(arr, divisor):
    answer = []
    
    for i in arr :
        if i % divisor == 0:
            answer.append(i)
    
    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
        
    return answer

# 다른 사람 풀이 
## 리스트 컴프리헨션을 이용한 방법 로직은 동일
def solution(arr, divisor):
    answer = []
    
    answer = sorted([n for n in arr if n % divisor == 0]) or [-1]
        
    return answer