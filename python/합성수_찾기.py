# 1부터 시작하여 약수의 개수 찾기
# 약수 개수가 3 이상인 경우 찾기

def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        if divisor >= 3:
            answer += 1
            
    return answer