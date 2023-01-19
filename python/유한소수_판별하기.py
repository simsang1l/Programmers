# <다른 사람의 풀이>
## 2, 5의 소인수로만 구성되어 있는 특징을 이용한 풀이
from math import gcd

def solution(a, b):
    answer = 0
    
    b //= gcd(a, b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    if b == 1 :
        answer = 1
    else :
        answer = 2
    
    return answer


# <나의 풀이, 테스트 케이스 2건 실패>

from math import gcd, sqrt

def primenumber(x):
    for i in range(2, int(sqrt(x) + 1) ):
        if x % i == 0:
            return 0
    return 1


def solution(a, b):
    answer = 0
    
    # 1. 기약분수인가?
        ## 아니라면 기약분수 만들기
            ### 최대공약수 이용
    # 2. 분모의 소인수가 2, 5만 있는가?
        ## 소인수 : 자연수를 나누어 떨어뜨리는 약수 중 소수
        ## 1. 약수 찾기
        ## 2. 소수인지 판별
            ### 제곱근에 해당하는 숫자가 나누어 떨어지지 않으면 소수임
                #### 짝지어지기 때문 ex) 8약수구할때 1 x 8, 2 x 4, 4 x 2, 8 x 2 ...
    
    gcd_val = gcd(a, b)
    divide_val = []
    
    if gcd_val == 1 :
        pass
    else :
        a = int(a / gcd_val)
        b = int(b / gcd_val)
      
    
    b의 약수가 소수
    for i in range(b, 1, -1):
        if b % i == 0 and primenumber(i) == 1:
            divide_val.append(i)
            
    divide_val.sort()

    if divide_val == [2, 5] or divide_val == [2] or divide_val == [5]:
        answer = 1
    else : 
        answer = 2
        
    return answer