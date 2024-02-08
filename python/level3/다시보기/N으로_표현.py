def solution(N, number):
    answer = 0
    dp = [set([int(str(N)*i)]) for i in range(1, 9)]
    print(dp)
    for i in range(8):
        for j in range(i):
            for num1 in dp[j]:
                # i - j
                for num2 in dp[i-j-1]:
                    print(i, j, num1, num2)    
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                    print(dp)    
        if number in dp[i]:
            return i + 1
    
    return -1

solution(5, 12)