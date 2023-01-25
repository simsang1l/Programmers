# 좌표가 음수일 때 음수와 비교도 필요함!

def solution(keyinput, board):
    answer = [0, 0]

    for value in keyinput:

        if value == 'left' and -(answer[0]) < board[0]//2 :
            answer[0] += -1
        elif value == 'right' and (answer[0]) < board[0]//2 :
            answer[0] += 1
        elif value == 'up' and (answer[1]) < board[1]//2 :
            answer[1] += 1
        elif value == 'down' and -(answer[1]) < board[1]//2 :
            answer[1] += -1
            
            
    return answer