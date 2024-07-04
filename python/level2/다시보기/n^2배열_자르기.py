"""
정답을 구하기 위해선 모든 원소가 있는 1차원 배열의 left index부터 right index의 값이 포함되어야 함
따라서 원소 개수를 index 번호처럼 이용하여 left 와 right에 해당하는 원소만 answer에 넣어줬음
left가 0 이라면 최대 10^7만큼 되니 시간초과가 될 가능성 높음
"""

# 테스트 1 ~ 테스트 11 통과, 테스트 12 ~ 테스트 20 시간초과
def solution(n, left, right):
    answer = []
    cnt = 0
    
    for i in range(n):
        num = i + 1
        for j in range(n):
            if num <= i+1 and j <= i:
                pass
            else :
                num += 1
            if cnt > right + 1:
                break
            
            if left <= cnt <= right:
                answer.append(num)
                
            cnt += 1

    return answer


# 다른 사람 풀이
"""
2차원 배열을 1차원 배열로 변환한다면
1차원 배열에서의 인덱스는 이렇게 구할 수 있음
index = i x n + j
여기서 i, j는 좌표값, n은 배열의 크기

1차원 배열의 인덱스를 이용하면 2차원 배열의 행과 열로 변환할 수 있음
row = k//n
col = k % n
"""
def solution(n, left, right):
    answer = []
    for k in range(left, right + 1):
        row = k // n
        col = k % n
        answer.append(max(row, col) + 1)
    return answer
