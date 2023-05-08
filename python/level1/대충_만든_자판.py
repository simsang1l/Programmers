def solution(keymap, targets):
    answer = []
    key = {}
    for i in keymap : 
        for idx, j in enumerate(i):
            if j not in key :
                key[j] = [idx + 1]
            else :
                key[j].append(idx + 1)
    
    for i in targets :
        score = 0
        for j in i :
            if j in key:
                score += min(key[j])
            elif j not in key :
                answer.append(-1)
                break
        else :
            answer.append(score)
        
    return answer

# 다른 사람 풀이
## min값을 굳이 list를 만들 필요가 없었다 ...!

def solution(keymap, targets):
    answer = []
    key = {}
    for i in keymap : 
        for idx, j in enumerate(i):
            if j not in key :
                key[j] = idx + 1
            else :
                key[j] = min(key[j], idx + 1)
    
    for i in targets :
        score = 0
        for j in i :
            if j not in key :
                score = -1
                break
            score += key[j]
        answer.append(score)
        
    return answer