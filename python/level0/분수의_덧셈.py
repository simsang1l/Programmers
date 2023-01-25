# 가장 빠른 ver
import math

def solution(denum1, num1, denum2, num2):
    answer = []
    # 1. 두 분수의 합 계산(일단 기약분수 따지지 않고)
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 * num2
    
    # 2. 최대공약수 계산
    gcd_value = math.gcd(boonmo, boonja)
            
    # 3. gcd로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]

    
    return answer

# gcd직접 구현 ver
def gcd(a, b):
    if a % b == 0:
        return b
    else :
        return gcd(b, a%b)

def solution(denum1, num1, denum2, num2):
    answer = []
    # 1. 두 분수의 합 계산(일단 기약분수 따지지 않고)
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 * num2
    
    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)
            
    # 3. gcd로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]

    
    return answer