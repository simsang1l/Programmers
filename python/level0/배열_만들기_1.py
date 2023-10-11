def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0 :
            answer.append(i)
    return answer

# 다른 사람 풀이
## k에서 시작하여 k씩 증가한 값에 대해서만 비교!
def solution(n, k):
    return [i for i in range(k,n+1,k)]