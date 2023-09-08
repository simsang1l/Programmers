def solution(x):
    answer = True
    num_lst = [int(i) for i in str(x)]

    if x % sum(num_lst) == 0 :
        answer = True
    else :
        answer = False
        
        
    return answer

## 다른 사람 풀이 

def solution(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0