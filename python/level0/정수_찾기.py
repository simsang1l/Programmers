def solution(num_list, n):
    answer = 0
    if n in num_list:
        answer = 1
    return answer

# 다른 사람 풀이
def solution(num_list, n):
    return int(n in num_list)