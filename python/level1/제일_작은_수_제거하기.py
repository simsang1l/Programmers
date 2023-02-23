# arr 정렬 후 가장 작은 값 추출
# arr에서 가장 작은값만 제거
def solution(arr):
    answer = []
    
    if len(arr) == 1 :
        answer = [-1]
    else :
        val0 = min(arr)
        arr.remove(val0)
        answer = arr
        
    return answer

## 다른사람 풀이
# 비슷하지만 다른코드, index 접근하는 방법
def solution(arr):
    if not len(arr) > 1 :
        return [-1]
    arr.pop(arr.index(min(arr)))

    return arr