def solution(n):
    answer = []
    # 1부터 찾아가니까 정렬도 필요 없음
    # n이 엄청 큰 숫자라면 못 쓰지 않을까?
    
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
            
    return answer