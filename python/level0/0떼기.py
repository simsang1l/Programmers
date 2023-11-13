def solution(n_str):
    answer = ''
    v = 0
    if n_str[0] != '0' :
        answer = n_str
    else :
        for i in range(len(n_str)):
            if n_str[i] != '0' :
                v = i
                break

        answer = n_str[int(v):]
    return answer

    
# 다른 사람 풀이
# lstrip이란게 있었네 ?
def solution(n_str):
    return n_str.lstrip('0')