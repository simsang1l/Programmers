def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
            
    return answer

# 다른 사람 풀이
def solution(n):
    answer = next(i for i in range(2, n) if n%i == 1)
            
    return answer