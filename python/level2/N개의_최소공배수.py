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