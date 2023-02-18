# 가장 단순한 방법..!
def solution(n):
    answer = 0
    div_lst = []
    
    for i in range(1, n+1) :
        if n % i == 0 :
            div_lst.append(i)
            
    answer = sum(div_lst)
    
    return answer

# 조금 더 파이썬스럽게
# 리스트 컴프리헨션이용
def solution(n):
    answer = 0

    answer = sum([i for i in range(1, n+1) if n % i == 0])
    
    return answer

# 다른사람 풀이
## num // 2 하여 2로 나눈 값보다 큰 값중 약수는 num 그 자체밖에 없음 이용
## 시간 절약
def solution(n):
    answer = 0

    answer = n + sum([i for i in range(1, (n//2) + 1) if n % i == 0])
    
    return answer