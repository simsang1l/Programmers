# 예제는 맞았으나 테스트에서 모두 실패 및 런타임 에러
"""
코드 문제점
1. m, n은 좌표 반대로 생각해야한다. row, col이라면 n = row, col = m 이다.
2. result[i][j]는 result[i-1][j] + result[i][j-1]이다.
"""
def solution(m, n, puddles):
    answer = 0
    # 동적 프로그래밍
    # 여러 경우가 나올 수 있는 곳이 있다. 이럴 땐 min값 필요
    # 각 좌표별 소모되는 비용 입력
    
    # 크기에 맞게 0으로 초기화 및 웅덩이는 -1로 표시
    result = [[0 for i in range(m)] for j in range(n)]
    for i in range(len(puddles)):
        result[puddles[i][0]-1][puddles[i][1]-1] = -1
    
    # 최단경로 개수 구하기
    for i in range(len(result)):
        for j in range(len(result[i])):
            # 왼쪽 혹은 위에 값이 없는지 확인
            # 둘 다 범위를 벗어나는 경우(시작점), 해당 지점이 -1인 경우
            if (i - 1 < 0 and j - 1 < 0) or result[i][j] == -1 :
                continue
            # 왼쪽은 있고 위쪽은 없는 경우
            elif j - 1 >= 0 and (i - 1 < 0 or result[i-1][j] == -1):
                result[i][j] = result[i][j-1] + 1
            # 위쪽은 있고 왼쪽은 없는 경우
            elif i - 1 >= 0 and (j - 1 < 0 or result[i][j-1] == -1):
                result[i][j] = result[i-1][j] + 1
            # 위쪽과 왼쪽 모두 있는 경우
            elif result[i-1][j] != -1 or result[i][j-1] != -1:
                result[i][j] = min(result[i-1][j], result[i][j-1]) + 1
            # 위쪽과 왼쪽 모두 웅덩이인 경우
            elif result[i-1][j] == -1 or result[i][j-1] == -1:
                result[i][j] == -1
                
    answer = min(result[n-2][m-1], result[n-1][m-2]) % 1000000007
            
    return answer


# 다른 사람 풀이
# ChatGPT
def solution(m, n, puddles):
    # 격자 초기화
    grid = [[0] * m for _ in range(n)]
    # 시작점 초기화
    grid[0][0] = 1
    
    # 웅덩이 표시 (주의: 입력이 [열, 행] 순서로 주어짐)
    for x, y in puddles:
        grid[y-1][x-1] = -1
    
    for i in range(n):
        for j in range(m):
            # 웅덩이는 건너뛰기
            if grid[i][j] == -1:
                continue
            # 왼쪽에서 오는 경우
            if j > 0 and grid[i][j-1] != -1:
                grid[i][j] += grid[i][j-1]
            # 위쪽에서 오는 경우
            if i > 0 and grid[i-1][j] != -1:
                grid[i][j] += grid[i-1][j]
                
    # 학교까지의 경로 수 반환, 웅덩이 때문에 갈 수 없는 경우 0 처리
    return grid[n-1][m-1] % 1000000007 if grid[n-1][m-1] != -1 else 0