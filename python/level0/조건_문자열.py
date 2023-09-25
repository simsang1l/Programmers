def solution(ineq, eq, n, m):
    answer = 0
    
    if (ineq == '>') & (eq == '='):
        if n >= m :
            answer = 1
    elif (ineq == '>') & (eq == '!'):
        if n > m :
            answer = 1
    elif (ineq == '<') & (eq == '='):
        if n <= m :
            answer = 1
    elif (ineq == '<') & (eq == '!'):
        if n < m :
            answer = 1
            
    return answer