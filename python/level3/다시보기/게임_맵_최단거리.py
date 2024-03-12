# 알쏭달쏭 BFS, 왜 어려운겨
from collections import deque

def solution(maps):
    answer = 0
    # 좌, 우, 상, 하 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        
        # 주어진 map의 크기, n은 행 개수, m은 열 개수
        n = len(maps)
        m = len(maps[0])
        
        # 좌, 우, 상, 하로 갈 수 있는 길인지 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 갈 수 있는 길인지 판단
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    answer = maps[n-1][m-1]
    # 목적지까지 연결이 안되어 있는 경우
    if answer  == 1 :
        answer = -1
        
    return answer