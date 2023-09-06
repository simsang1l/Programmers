def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    if a + b > b + a:
        answer = int(a + b)
    else :
        answer = int(b + a)
        
    return answer

# 다른사람 풀이

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))