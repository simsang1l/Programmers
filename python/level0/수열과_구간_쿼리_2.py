def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = []
        for i in range(s, e+1):
            if e <= k:
                break
            elif arr[i] > k:
                temp.append(arr[i])
        if temp :
            value = min(temp)
            answer.append(value)
        else :
            answer.append(-1)
        
    return answer