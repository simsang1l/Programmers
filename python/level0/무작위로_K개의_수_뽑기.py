def solution(arr, k):
    answer = []
    for i in arr :
        if i not in answer :
            answer.append(i)
        
        if len(answer) == k :
            break

    if k - len(answer) > 0 :
        for i in range(k - len(answer)):
            answer.append(-1)
    elif k - len(answer) < 0:
        answer = answer[:k]
        
         
    return answer