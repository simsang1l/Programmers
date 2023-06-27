# 3진수를 구하는 방법과 유사하다.
# 3의 배수일 경우 0으로 나누어 떨어져 4를 표현할 수 없음
# 따라서 n에 -1을 더해줌으로서 index를 접근할 수 있다.

def solution(n):
    answer = ''
    while n > 0 :
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
        
    return answer
    