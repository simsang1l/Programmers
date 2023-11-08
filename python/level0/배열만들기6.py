def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if len(answer) == 0:
            answer.append(arr[i])
        elif answer[-1] == arr[i] :
            answer.pop()
        elif answer [-1] != arr[i]:
            answer.append(arr[i])
    if len(answer) == 0 :
        answer = [-1]
    
    return answer