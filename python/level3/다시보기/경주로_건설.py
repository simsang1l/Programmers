# 나의 에러코드
# BFS, 코너인가?판별 후  비용계산
# 직선은 100원, 코너는 500원
# 코너: 현재 위치에서 옆과 위/아래의 이동이 가능한경우! -> 방향이 바뀌는경우

from collections import deque

def solution(board):
    answer = 0
    # 좌, 우, 상, 하 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)
    closed = [[-1 for _ in range(n)] for _ in range(n)]
    print(closed)
    queue = deque([(0, 0, -1)]) # 시작위치 넣기
    
    while queue:
        x, y, d = queue.popleft() # x, y, direction
        n = len(board)
        
        if x == n - 1 and y == n - 1:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if d != i and d != -1:
                    board[nx][ny] = board[x][y] + 600
                else :
                    board[nx][ny] = board[x][y] + 100
                queue.append((nx, ny, i))
    print(board)
    answer = board[n-1][n-1]
    return answer