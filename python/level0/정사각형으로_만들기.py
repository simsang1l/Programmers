def solution(arr):
    answer = []
    
    if len(arr) == len(arr[0]):
        answer = arr
        return answer
    else :
        length = max(len(arr), len(arr[0]))
        
        # 1. 일단 열의수를 맞춘다
        # 2. 행의 수를 맞춘다
        for i in range(len(arr)):
            if len(arr[i]) < length:
                answer.append(arr[i] + [0]*(length - len(arr[i])))
            else :
                answer.append(arr[i])
                
        if length > len(arr):            
            for i in range(length - len(arr)):
                answer.append([0]*length)

            
    return answer


# 다른 사람 풀이
# arr의 모든 원소의 길이가 같기 때문에 가능!
def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])

    if num_rows > num_cols:
        for i in range(num_rows):
            arr[i] += [0] * (num_rows - num_cols)
    elif num_cols > num_rows:
        for i in range(num_cols - num_rows):
            arr.append([0] * num_cols)

    return arr