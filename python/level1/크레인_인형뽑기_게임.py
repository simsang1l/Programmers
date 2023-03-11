def solution(board, moves):
    answer = 0
    result = []
    
    for i in moves:
        position = 0
        
        while position < len(board):
            if board[position][i-1] != 0 :
                result.append(board[position][i-1])
                board[position][i-1] = 0
                break
            else :
                position += 1
        if len(result)  >= 2:
            
            if result[-1] == result [-2]:
                result.pop()
                result.pop()        
                answer += 2
        
            
    return answer

## 다른사람 풀이
def solution(board, moves):
    # 0이 아닌 값만 추출하, 가장 위에있는 인형을 보여주는 형태
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a