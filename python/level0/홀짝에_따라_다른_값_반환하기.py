def solution(n):
    answer = 0
    if n % 2 == 0 :
        answer = sum([i**2 for i in range(1, n+1) if i % 2 == 0])
    else :
        answer = sum([i for i in range(1, n+1) if i % 2 != 0 ])
    return answer

# 다른 사람 풀이
# 시작점을 이용해 2칸씩 이동하면 되네
def solution(n):
    answer = 0
    if n%2:
        for i in range(1,n+1,2):
            answer += i
    else:
        for i in range(2,n+1,2):
            answer += i**2
    return answer