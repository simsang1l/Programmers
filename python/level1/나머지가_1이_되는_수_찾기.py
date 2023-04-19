def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
            
    return answer

# 다른 사람 풀이
## next(): 반복할 수 있을 때 까지 값을 출력하고, 반복이 끝나면 기본값 출력
def solution(n):
    answer = next(i for i in range(2, n) if n%i == 1)
            
    return answer