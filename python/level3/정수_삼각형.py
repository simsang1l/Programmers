def solution(triangle):
    # 삼각형의 높이
    n = len(triangle)
    
    # 동적 계획법을 위한 리스트 초기화
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    # 동적 계획법 적용
    # 양 끝을 계산하고, 중간에 겹치는 부분은 max값만 가지게 한다
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    # 마지막 줄에서 최대값 반환
    answer = max(dp[n-1])
    return answer


# 다른 사람 풀이
# 가장 아래층에서 높은층으로 올라가는 방법
# 아직 익숙치 않다 ..
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer