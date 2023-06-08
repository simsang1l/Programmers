from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    # 시작위치 좌표 넣기
    queue.append((0, 0))
    
    # queue가 빌 때까지 반복
    while queue :
        x, y = queue.popleft()
        
        # 상하좌우 칸 확인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵을 벗어나면 무시하기
            if nx <0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
            
            # 벽이면 무시하기
            if maps[nx][ny] == 0: continue
            
            # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
            
                
    # 상대 팀 진영(제일 오른쪽 아래 칸) 까지의 거리 반환
    answer = maps[len(maps) - 1][len(maps[0]) - 1]
    
    if answer == 1 :
        answer = -1
        
    return answer