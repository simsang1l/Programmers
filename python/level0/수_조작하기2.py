
def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        calc = numLog[i+1] - numLog[i]
        if calc == 1:
            answer += 'w'
        elif calc == -1:
            answer += 's'
        elif calc == 10:
            answer += 'd'
        elif calc == -10:
            answer += 'a'
            
    return answer

# 다른 사람 풀이
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res