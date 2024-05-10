"""
wires가 송전탑간 연결되었다는 정보를 가지고있다.
따라서 wires에 첫번째 값, 두번째 값을 기준으로 bfs를 진행하면 송전탑의 개수를 알 수 있을 것 같다.
이 방법을 연결된 전선마다 적용해보면 송전탑 개수의 차이(절대값)의 최소값(두 전령망이 갖게되는 송전탑의 개수를 비슷하게 맞춘다)을 구할 수 있음
ex. 
    1번 예제에서 wires의 첫번째 값은 [1, 3]
    1, 3번 송전탑의 전선을 끊었다고 할 때, 1번 송전탑에서 BFS, 3번 송전탑에서 BFS하여 송전탑 개수 구하기
    그 다음 두 전령망간의 차이의 최소값 구하기
"""

from collections import deque

def bfs(queue, n, graph):
    visited = [0 for _ in range(n+1)]
    
    cnt = 1
    
    while queue:
        now = queue.popleft()
        visited[now] = 1
        
        for i in graph[now]:
            if visited[i] == 0 :
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt
    
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    for s, e in wires :
        graph[s].remove(e)
        graph[e].remove(s)
    
        answer = min(abs(bfs(deque([s]), n, graph) - bfs(deque([e]), n, graph)), answer)
        
        graph[s].append(e)
        graph[e].append(s)
        
    return answer