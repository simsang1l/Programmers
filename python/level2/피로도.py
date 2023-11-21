# 순열을 이용하여 모든 경우에 대해 조사하여 정답 구하기
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    pt = permutations(dungeons, len(dungeons))
    lst = []
    
    for i in pt :
        current_cost = k
        cnt = 0
        for m_fatigue, fatigue_c in i:
            if current_cost >= m_fatigue:
                current_cost -= fatigue_c
                cnt += 1
            else :
                break
        lst.append(cnt)
        
    answer = max(lst)

    return answer

# 다른 사람 풀이
# dfs, 재귀함수로 푸는 방법
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer