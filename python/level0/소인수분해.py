# 소수로 n을 나눠 나간다
# 소수 2로 나눠 나누어 떨어지지 않을 때 까지 나눈 후 1씩 증가하여 나누기

    
def solution(n):
    answer = []
    prime_set = []
    i = 2
    while i <= n :
        if n % i == 0 :
            prime_set.append(i)
            n = n//i
        else :
            i += 1
    
    for i in prime_set :
        if i not in answer :
            answer.append(i)
    
    return answer