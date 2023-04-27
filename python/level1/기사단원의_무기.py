# 테스트11 ~ 테스트16, 테스트18, 24, 25 시간초과 
def cnt (num):
    answer = 0
    
    if num == 1 :
        answer = 1
        return answer 
    
    else :
        for i in range(2, num):
            if num % i == 0:
                answer += 1
                
        return answer + 2
        
    
def solution(number, limit, power):
    answer = 0
    num = [cnt(i) for i in range(1, number+1)]
    for i in num :
        if i <= limit:
            answer += i
        else :
            answer += power
            
    return answer

# 약수를 구하는 방법을 개선하여 해결
def getMyDivisor (num):
    answer = 0
    
    for i in range(1, int(num**(1/2)) + 1):
        if (num % i == 0):
            answer += 1
            if i**2 != num :
                answer += 1
    return answer     
    
def solution(number, limit, power):
    answer = 0
    num = [getMyDivisor(i) for i in range(1, number+1)]
    for i in num :
        if i <= limit:
            answer += i
        else :
            answer += power
            
    return answer
