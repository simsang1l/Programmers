# n을 제곱근 취하면 제곱근을 알 수 있다.
def solution(n):
    answer = 0
    num = n ** 0.5

    if num == int(num):
        answer = (num+1) ** 2
    else:
        answer = -1

    return answer

## 다른 사람 풀이 
def solution(n):
    sqrt = n**(1/2)

    if sqrt % 1 == 0:
        answer = (sqrt + 1)**2
    else :
        answer = -1


    return answer