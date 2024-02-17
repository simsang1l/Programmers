# n == 나 + 내가 이긴 상대 + 내가 패한 상대
from collections import deque

def find_person(winner, loser, node) :
    q = deque()
    visited = [False] * (len(winner)+1)
    
    for i in winner[node] :
        q.append(i)
        
    while q :
        x = q.popleft()
        for i in winner[x] : 
            if not visited[i] : # 아직 탐색하지 않은 선수라면
                visited[i] = True
                winner[node].add(i) # 내가 이길 수 있는 사람에 i를 추가
                loser[i].add(node) # i가 지는 사람에 나를 추가
                q.append(i)
                
def solution(n, results):
    answer = 0
    winner = [set([]) for i in range(n+1)]
    loser = [set([]) for i in range(n+1)]
    
    for w, l in results:
        winner[w].add(l)
        loser[l].add(w)
    
    # 경기를 하지 않았지만 나를 이긴사람을 이긴 사람목록에 추가
    for i in range(1, n+1):
        find_person(winner, loser, i)

    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) + 1 == n :
            answer += 1
            
    return answer