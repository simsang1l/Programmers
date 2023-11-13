def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0 :
        for i, v in enumerate(arr):
            if i % 2 != 0 :
                answer.append(v + n)
            else : 
                answer.append(v)
    else :
        for i, v in enumerate(arr):
            if i % 2 == 0 :
                answer.append(v + n)
            else : 
                answer.append(v)
                
    return answer
    
# 다른 사람 풀이
# 바꿔야하는 index부분만 변경하므로서 시간 단축!
def solution(arr, n):
    N=len(arr)
    if N%2:
        for i in range(0,N,2): arr[i]+=n
    else:
        for i in range(1,N,2): arr[i]+=n
    return arr