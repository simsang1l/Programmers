import math

def solution(n, m):
    answer = []
    lcm = n * m / math.gcd(n, m)
    gcd_val = math.gcd(n, m)
    
    answer = [gcd_val, lcm]
    
    return answer

## 다른사람 풀이

# for문 이용하기
def solution(n, m):
    answer = []  
    
    ## 최대공약수 구하기
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i) # gcd
            break
    ## 최소공배수 구하기
    for j in range(max(n, m), (n*m)+1):
        if j % n == 0 and j % m == 0:
            answer.append(j) # lcm
            break
    
    
    return answer

# 유클리드 호제법
# x, y의 최대공약수는 y, r의 최대 공약수와 같다(x % y == r)
def gcd(x, y):
    while y : # y가 True일 때 = 자연수 일 때 =  (a % b != 0)
        x, y = y, x%y
    return x

def lcm(x, y):
    result = (x * y)//gcd(x, y)
    return result
    
def solution(n, m):
    answer = []
    
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    
    return answer