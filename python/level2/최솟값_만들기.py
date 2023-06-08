def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    
    for i in A :
        for j in range(len(B)) :
            low = i * B[j]
            B.pop(j)
            break
  
        answer += low

    return answer

# 이렇게 하는게 더 빠르겠다!
def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    
    for i in A :
        low = i * B[0]
        B.pop(0)
  
        answer += low

    return answer