# 답지를 보면 이해가 잘 가지만 혼자서는 못 푼 문제..

# reference: https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp
    # "파이썬이 1초에 가능한 연산수가 약 2천만임, 3중 for문을 썼을 때 이 문제에 대해서는 10억개의 연산 필요. 따라서 DP 이용!"" 이 말이 논리적이라고 생각돼 좋았다.
    # DP(Dynamic programming): 전체를 한번에 풀기 어려우니 부분적으로 문제를 푼다. 부분 문제의 답을 저장해두고 필요에 따라 바로 사용하게끔 하는 방법.

# answer**2인 이유??
    # 넓이 계산을 위해

def solution(board):
    
    dp = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    global_max = 0
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):

            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                if dp[i][j] > global_max :
                    global_max = dp[i][j]


    return global_max**2