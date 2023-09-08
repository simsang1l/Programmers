def solution(n):
    answer = 0
    lst = [1, 1]
    
    if n == 0 :
        answer = 0
    elif n == 1 :
        answer = 1
    else :
        for i in range(2, n):
            lst.append(lst[i-2] + lst[i-1])

        answer = lst[-1] % 1234567
        
    return answer

# 다른 사람 풀이 
def solution(n):
    f_list = [0,1]
    for i in range(2,n+1):
        f_list.append((f_list[i-2]%1234567+f_list[i-1]%1234567)%1234567)
    return f_list[-1]