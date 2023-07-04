# 따로 for문으로 접근하기보단 index로 직접접근도 할 수 있다
def solution(msg):
    answer = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = {al: idx+1 for idx, al in enumerate(alpha)}
    w, c = 0, 0

    while True:
        c += 1
        if c == len(msg):
            answer.append(index[msg[w:c]])
            break
        if msg[w:c+1] not in index:
            index[msg[w:c+1]] = len(index) + 1
            answer.append(index[msg[w:c]])
            w = c
        
    
    return answer