def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    # 초기 방향 설정, 오른쪽
    dx, dy  = 0, 1 
    for i in range(1,n**2+1):
        answer[x][y] = i
        # 다음 위치
        next_x, next_y = x + dx , y + dy
        
        # 범위 벗어나거나 채워진 경우 방향 바꾸기
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or answer[next_x][next_y] != 0:
            dx, dy = dy, -dx
            next_x, next_y = x + dx , y + dy
        
        x, y = next_x, next_y
        
    return answer

# 다른 사람 풀이
def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer