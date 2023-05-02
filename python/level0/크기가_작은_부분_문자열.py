def solution(t, p):
    answer = 0
    p_len, t_len = len(p), len(t)
    lst = []
    
    for idx, i in enumerate(t):
        if idx + p_len - 1 == t_len:
            break
        else :
            lst.append(int(t[idx : idx + p_len]))
            
    answer = [x for x in lst if x <= int(p)]
    answer = len(answer)
    
    return answer

# 다른 사람 풀이
def solution(t, p):
    answer = 0
    p_len, t_len = len(p), len(t)
    
    for i in range(t_len - p_len + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer