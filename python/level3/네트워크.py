# visited 기준으로 bfs
# 1번 노드 부터 시작해서 bfs진행하고, 방문 안한 node들에 대해 bfs계속 진행
from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
        
    while queue:
        now = queue.popleft()

        for node in graph[now]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1
                    
    return visited                    
    
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n+1)]
    
    # node간 연결 정보가 있는 graph 만들기
    for idx, net in enumerate(computers):
        for i, node in enumerate(net):
            if idx == i :
                continue
            elif node == 1 :
                graph[idx+1].append(i+1)
    
    for i in range(1, n+1):
        if i == 1:
            visited = bfs(i, graph, visited)
            answer += 1
        elif visited[i] == 0 :
            visited = bfs(i, graph, visited)
            answer += 1
    
    return answer