def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    
    while True:
        # 같은 모양의 2X2 블록을 찾으면 remove 배열에 1로 표시
        remove = [[0]*n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    remove[i][j], remove[i][j + 1], remove[i + 1][j], remove[i + 1][j + 1] = 1, 1, 1, 1
                    
        # 지워진 블록 개수 세기
        count = 0
        for i in range(m): 
            count += sum(remove[i])
        answer += count
        
        # 지워진 블록이 없을 경우 break
        if count == 0: 
            break
            
        # 지워진 블록을 위의 블록으로 채우기
        for i in range(m - 1, -1, -1):
            for j in range(n):

                if remove[i][j] == 1:
                    x = i - 1

                    while x >= 0 and remove[x][j] == 1: 
                        x -= 1
                    
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1

    return answer
            