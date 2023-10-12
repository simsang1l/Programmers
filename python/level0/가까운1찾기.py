# 테스트케이스 
# arr = [1, 1, 1, 1], idx = 1, result = 1 를 생각해보면 오류 없을 것임
def solution(arr, idx):
    answer = -1
    for i in range(len(arr) - idx):
        if arr[idx+i] == 1 :
            answer = idx + i
            break
            
    return answer

# 다른 사람 풀이
# arr.index(1, idx) 1의 값을 가지는 index를 idx부터 시작해서 arr에서 찾아라 라는 뜻임
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer