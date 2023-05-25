# while, for문으로는 시간초과 발생
# 문자열 길이가 백만 이하의 자연수라서 그런듯
def solution(s):
    start = len(s)
    
    while start > 0:
        start = len(s)
        for i in range(start - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i+2:]
                break
                
        if start == len(s):
            answer = 0
            break
            
    if len(s) == 0 :
        answer = 1

    return answer

# stack 이용
def solution(s):
    stack = []
    
    for i in range(len(s)):
        if not stack :
            stack.append(s[i])
        else : 
            if stack[-1] == s[i]:
                stack.pop()
            else :
                stack.append(s[i])
            
    if stack :
        answer = 0
    else :
        answer = 1

    return answer
