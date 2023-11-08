def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
        
    return answer

# 다른 사람 풀이
# map을 이용하기~
def solution(num_str):
    return sum(map(int, list(num_str)))