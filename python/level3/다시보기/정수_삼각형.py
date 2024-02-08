"""
될거 같은데 구현이 잘 안됐다..
"""
def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])) :
            if j == 0 : # 왼쪽 끝일때
                triangle[i][j] += triangle[i-1][0] # 이전 층의 왼쪽 끝값 더하기
            elif j == len(triangle[i]) - 1: # 오른쪽 끝일때
                triangle[i][j] += triangle[i-1][-1] # 이전 층의 오른쪽 끝 값 더하기
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1]) # 겹치는 부분은 더 큰 값 넣기
        print(triangle)
    print(triangle[-1])
    return answer