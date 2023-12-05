def solution(arr, k):
    answer = []
    if k % 2 == 0 :
        answer = [i+k for i in arr]
    else :
        answer = [i*k for i in arr]
    return answer
    
# 다른 사람 풀이
# 조건문을 한번에 처리해도 되는데!
def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]