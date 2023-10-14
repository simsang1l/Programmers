def solution(arr):
    answer = []
    start_idx = -1
    end_idx = 0
    
    for i in range(len(arr)) :
        if arr[i] == 2 and start_idx == -1:
            start_idx = i
        if arr[i] == 2 :
            end_idx = i
    if start_idx == -1 :
        answer = [-1]
    else :
        answer = arr[start_idx:end_idx+1]
    return answer

# 다른 사람 풀이
# 첫 2의 index와 마지막 2의 index를 찾는 코드!
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]