# 더 좋은 방법이 있겠지.. 

def solution(board):
    answer = 0
    bombs = []
    bx = [-1, -1, 0, 1, 1, 1, 0, -1]
    by = [0, -1, -1, -1, 0, 1, 1, 1]
    len_board = len(board) # 자주사용한다면 변수로 지정해주기만해도 속도 차이가 많이나는듯
    
    # 지뢰 매설 지역 찾기(1 찾기)
    for i in range(len_board) :
        for j in range(len_board) :
            if board[i][j] == 1 :
                bombs.append((i, j))
                
    # 1주위 위, 아래, 좌, 우 대각선 칸 찾아 위험지역으로 분류(= 폭탄 설치)
    # 1이 있는 좌표가 (a, b) 일때
    ## 위 : (a-1, b)
    ## 아래 : (a+1, b)
    ## 왼 : (a, b-1)
    ## 오 : (a, b+1)
    ## 왼위 대각: (a-1, b-1)
    ## 오위 대각: (a-1, b+1)
    ## 왼아래 대각: (a+1, b-1)
    ## 오아래 대각: (a+1, b+1)
    for x, y in bombs:
        for i in range(8):
            nx = x + bx[i]
            ny = y + by[i]
            if 0 <= nx < len_board and 0 <= ny < len_board:
                board[nx][ny] = 1
                
    # 안전 지역 칸 수 세기            
    for x in range(len_board):
        for y in range(len_board):
            if board[x][y] == 0:
                answer += 1
                
    return answer