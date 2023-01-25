def solution(A, B):
    answer = 0
        
    while answer != len(A):
        if A == B :
            break
        A = A[-1] + A[:-1]
        print(A)
        answer += 1
    
    if A != B :
        answer = -1
        
        
    return answer