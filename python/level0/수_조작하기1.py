def solution(n, control):
    answer = 0
    
    for i in control :
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10
    answer = n
    
    return answer

# 다른 사람 풀이 
# list의 zip이용
# list 두개를 이용한 dictionary만들기
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])