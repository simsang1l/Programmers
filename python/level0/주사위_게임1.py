def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0 :
        answer = a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0 :
        answer = 2 * (a + b)
    else :
        answer = abs(a - b)
    
    
    return answer

# 다른 사람 풀이
# True and True 같은 논리연산자 이용한 방법? 꼭 == 0이 나올필욘 없다
def solution(a, b):
    if a % 2 and b % 2:
        return a ** 2 + b ** 2
    elif not a % 2 and not b % 2:
        return abs(a - b)
    else:
        return 2 * (a + b)