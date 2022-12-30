# 팩토리얼 계산
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else :
        return 1
        
def solution(n):
    answer = 0
    i = 0
    # factorial(i)가 n보다 크면 factorial(i-1)이 만족하는 가장 큰 정수임
    while True:
        if n < factorial(i) :
            answer = i - 1
            break
        
        i += 1 
        
    return answer