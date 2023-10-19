def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        m = int(i[s:s+l])
        if m > k :
            answer.append(m)
    
    return answer