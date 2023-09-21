def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        state = 0
        for s in str(i) :
            if s in ['0', '5']:
                state = 1
            else :
                state = 0
                break
        if state == 1 :
            answer.append(i)

    if not answer :
        answer.append(-1)
                
    
    return answer

## 다른사람풀이
def solution(l, r):
    answer = []
    n = [int(bin(x)[2:])*5 for x in range(1,65)]
    for i in n:
        if i >= l and i <= r:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer

    