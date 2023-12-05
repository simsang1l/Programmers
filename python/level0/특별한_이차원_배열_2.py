def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer = 1
            else :
                return 0
    
    return answer

 # 다른 사람 풀이
 # 내 풀이와 비슷하지만 조금 더 깔끔한 풀이
 def solution(arr):
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0

    return 1