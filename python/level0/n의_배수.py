def solution(num, n):
    answer = 0
    if num % n == 0 :
        answer = 1
    return answer

# 다른사람풀이
def solution(num, n):
    return int(not(num % n))