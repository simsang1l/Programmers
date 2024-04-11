# 테스트 5, 6, 8, 9, 10, 11, 13, 14 시간초과
# k의 범위가 1,000,000 이므로 k=1이라면 좌표 개수가 1,000,000 * 1,000,000개 있을 수 있음
# 모든 경우의 수를 다 구하니 발생할 것으로 생각됨 
def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        for j in range(0, d+1, k):
            # 직선거리가 d보다 작아야 함
            if (i**2 + j**2)**0.5 <= d :
                answer += 1

    return answer

# 질문하기 힌트를 보고 풀었다.
# x**2 + y**2 = r**2을 이용하면 y의 최대값을 구할 수 있다. 이를 이용해서 y좌표의 개수를 알 수 있음
def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        y_square = d**2 - x**2
        max_y = int((y_square)**0.5)
        y_cnt = max_y // k + 1 # 좌표가 0일때도 포함시켜야 하기 때문에 1을 더해줌
        
        answer += y_cnt

    return answer