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

def solution(n):
    answer = 0
    # 피자 한판 6조각
    # 먹을 사람 n명
    ## answer : 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다
    
    # 1. 6과 n의 최소공배수를 구하면 피자 조각수 
    # 2. 피자조각수를 6으로 나누면 피자 판수
    
    piece = lcm(n, 6)
    answer = piece // 6
    
    return answer