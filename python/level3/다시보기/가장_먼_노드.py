from collections import deque

def solution(n, edge):
    answer = 0
    distance = [-1 for _ in range(n+1)] # 시작점에서 노드 간 거리를 구하려고 함
    
    graph = [[] for _ in range(n+1)]
    for s, e in edge: # index번 노드에 연결된 노드 정보 저장
        graph[s].append(e)
        graph[e].append(s)

    
    queue = deque([1]) # 출발 노드 설정
    distance[1] = 0 # 출발 노드의 최단거리를 0으로 설정
    
    # 1부터 BFS탐색하여 시작 노드와 거리 구하기
    while queue :
        now = queue.popleft()

        for i in graph[now]: # 인접한 노드와의 거리 계산하기
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1
    
    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance:
        if d == max(distance):
            answer += 1
    
    return answer