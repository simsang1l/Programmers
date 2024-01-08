# 재귀로 풀어보기
def collatz(n, step = 0):
    if step >= 500:
        return -1
    elif n == 1 :
        return step
    elif n % 2 == 0:
        return collatz(n//2, step + 1)
    else :
        return collatz(3 * n + 1, step + 1)
    
def solution(num):
    answer = 0
    
    answer = collatz(num)
        
    return answer

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
