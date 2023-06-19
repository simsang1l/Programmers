# 2번째 행 부터 다음 열의 값을 사용할 수 없다. 따라서 다른 열의 값을 더하면서 최대값을 계속 저장해나갈 수 있다.
## DP, 동적계획법에 대해 알 필요가 있다.
# 개념 이해 및 문제 풀이를 위한 글 (https://shanepark.tistory.com/183)
def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    
    answer = max(land[len(land) - 1])
    
    return answer

# 다른사람 풀이
def solution(land):
    
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])