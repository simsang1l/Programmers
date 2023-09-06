def solution(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0 :
        answer = 1
    return answer

# 다른사람풀이
def solution(number, n, m):
    return int(number%n == 0 and number%m == 0)
