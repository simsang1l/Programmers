from itertools import permutations

# 소수판별 최적화!
"""
1. 소수는 2를 제외하고는 모두 홀수이다
2. n이 소수가 아니라면 약수 중 적어도 하나는 n의 제곱근 이하임 따라서 제곱근까지 검사
"""
def isPrime(n):
    if n <= 1 :
        return False
    if n == 2 :
        return True
    if n % 2 == 0 : 
        return False
    
    sqrt_n = int(n**0.5) + 1 # range에서 종료값은 포함하지 않기 때문에 +1 적용
    for divisor in range(3, sqrt_n, 2): # 홀수만 확인해보면 되기 때문에 2계단 씩 적용되도록 함!
        if n % divisor == 0 :
            return False
        
    return True

def solution(numbers):
    answer = 0
    numbers = [i for i in numbers]
    lst = []
    
    # 가능한 경우 목록 lst에 저장
    for i in range(len(numbers)) :
        for j in list(permutations(numbers, i+1)):
            lst.append(int(''.join(j)))
    
    lst = set(lst)
    
    # 소수 판별
    for i in lst:
        if isPrime(i) :
            answer += 1
    
    return answer