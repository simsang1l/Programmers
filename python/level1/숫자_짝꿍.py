# 다른 사람 풀이
def solution(X, Y):
    answer = ''

    numx = {str(n):0 for n in range(10)}
    numy = {str(n):0 for n in range(10)}
    
    for x in X:
        numx[x] += 1
    
    for y in Y:
        numy[y] += 1
    
    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(numx[k], numy[k])
        
        if answer == '' and k == '0' and iternum != 0:
            return "0"
        
        answer = ''.join([answer, k*iternum])  
    
    if answer == '':
        return "-1"
    else:
        return answer



def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer