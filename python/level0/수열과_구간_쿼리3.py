def solution(arr, queries):
    answer = []
    for i, j in queries:
        first = arr[i]
        second = arr[j]
        
        arr[i] = second
        arr[j] = first
    answer = arr  
    return answer

# 다른 사람 풀이
# 파이썬에선 곧바로 값이 바뀌는구나
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr