def solution(n):
    answer = []
    answer.append(n)
    while n != 1 :
        if n % 2 == 0 :
            n /= 2
        else :
            n = 3 * n + 1
        answer.append(n)
    return answer

# 다른 사람 풀이
def solution(n):
    temp = []

    while True:
        if len(temp) == 0:
            temp.append(n)
        elif n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
            temp.append(n)
        elif n % 2 != 0:
            n = 3 * n + 1
            temp.append(n)

    return temp