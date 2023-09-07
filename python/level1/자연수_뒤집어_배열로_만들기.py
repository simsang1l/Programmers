def solution(n): 
    answer = []
    
    num = str(n)[::-1]
    answer = [int(i) for i in num]
    
    
    return answer

## 다른 사람 풀이 
## map 함수를 쓰면 간단하게 사용할 수 있겠군...
def solution(n):   
    answer = list(map(int, reversed(str(n))))
    
    
    return answer
