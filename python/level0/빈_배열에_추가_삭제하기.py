def solution(arr, flag):
    answer = []
    for a, f in zip(arr, flag):
        if f :
            for i in range(a*2):
                answer.append(a)
        else :
            for i in range(a):
                answer.pop()
        
    return answer