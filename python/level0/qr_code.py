def solution(q, r, code):
    answer = ''
    
    for i in range(len(code)):
        if i % q == r :
            answer += code[i]
        
    return answer

# 다른 사람 풀이
def solution(q, r, code):
    return code[r::q]