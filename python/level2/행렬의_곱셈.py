def solution(arr1, arr2):
    arr1_l, arr1_r = len(arr1), len(arr1[0])
    arr2_l, arr2_r = len(arr2), len(arr2[0])
    answer = [[0]* arr2_r for _ in range(arr1_l)]
    
    for k in range(arr1_l) :
        for i in range(arr2_r):
            for j in range(arr1_r):
                answer[k][i] += (arr1[k][j] * arr2[j][i])
        
    return answer