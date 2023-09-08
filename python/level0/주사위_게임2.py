def solution(a, b, c):
    answer = 0
    score = {1: (a + b + c)
            , 2: (a + b + c) * (a**2 + b**2 + c**2)
            , 3: (a + b + c) * (a**2 + b**2 + c**2)* (a**3 + b**3 + c**3)}
    
    if a == b == c:
        answer = score[3]
    elif a == b or b == c or a == c:
        answer = score[2]
    else :
        answer = score[1]
        
    return answer

# 다른 사람 풀이 
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)