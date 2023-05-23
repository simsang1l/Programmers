# 2로 나누어 떨어지지 않으면 1칸 이동후 순간이동을 해야함을 이용함
def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 != 0 :
            ans += 1
            
        n = n // 2

    return ans

# 다른 사람 풀이
def solution(n):
    return bin(n).count('1')