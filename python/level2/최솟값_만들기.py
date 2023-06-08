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