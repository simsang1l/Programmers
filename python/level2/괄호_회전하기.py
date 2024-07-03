"""
1. 왼쪽으로 x칸 만큼 회전
2. 올바른 괄호 문자열인지 판단
3. 2번 반복

** x는 len(s)미만이어야함
"""

def s_right(s):
    stack = []
    matching = {')': '(', ']':'[', '}':'{'}
    
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
        else :
            return False
    return len(stack) == 0

        
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        if s_right(rotated_s):
            answer += 1
    
    return answer