def solution(arr, intervals):
    answer = []
    for s, e in intervals :
        answer.extend(arr[s:e+1])
    return answer

# 다른 사람 풀이
## +로도 연결이 되는구나
def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1]
    return answer