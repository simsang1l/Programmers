def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        value = format(b | a, 'b').zfill(n)
        val = value.replace('1', '#').replace('0', ' ')
        
        answer.append(val)

    return answer

## 다른 사람 풀이 
