# 최대 공약수 구하기
def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

# 최소 공배수 구하기
def lcm(a, b):
    gcd_value = gcd(a, b)    
    if gcd_value == 0 : 
        return 0
    else :
        return abs((a * b) / gcd_value)
    
def solution(arr):
    answer = 0
    temp = arr[0]
    for i in range(1, len(arr)):
        temp = lcm(temp, arr[i])
    
    answer = temp
    
    return answer

# 다른 사람 풀이
## fractinos는 파이썬에서 유리수를 정확하게 계산하기 위한 모듈
## 유리수는 두 정수의 비율 또는 분수 형식으로 나타낼 수 있는 수를 말함

from fractions import gcd


def solution(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer) # 결국 두 수의 최소공배수 구하는 식

    return answer