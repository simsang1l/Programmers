def solution(array, commands):
    answer = []
    for i in commands:
        a = sorted(array[i[0]-1:i[1]])
        answer.append(a[i[2]-1])
        
    return answer

## 다른사람 풀이
