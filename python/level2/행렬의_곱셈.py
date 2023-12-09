def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            result = 0
            for s in range(len(arr2)):
                result += (arr1[i][s] * arr2[s][j])
            
            tmp.append(result)
        answer.append(tmp)
    
    return answer