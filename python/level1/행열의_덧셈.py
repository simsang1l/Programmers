import numpy as np

def solution(arr1, arr2):
    answer = np.array(arr1) + np.array(arr2)
    answer = answer.tolist()
    
    return answer

## 다른사람 풀이
def solution(arr1, arr2):

    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    
    return answer