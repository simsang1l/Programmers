# stack에 값을 계속 쌓고 ()쌍으로 stack에 쌓인다면 stack에서 pop 해주는 방법 이용
def solution(s):
    answer = True
    stack = []
    
    for i in s :     
        if len(stack) != 0 and stack[-1] == '(' and i == ')':
            stack.pop()
        else :
            stack.append(i)
            
    if len(stack) == 0:
        answer = True
    else :
        answer = False
        

    return answer