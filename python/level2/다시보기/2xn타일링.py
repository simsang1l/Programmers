# 점화식을 잘 못찾겠다 ㅎ하ㅏ..
## n=1 -> 1, n=2 -> 2, n=3 -> 3, n=4 -> 5 ...
## f(n) = f(n-1) + f(n-2)이런 형태의 점화식을 가짐

def solution(n):
    answer = 0
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
        
    answer = dp[n-1]
    
    return answer