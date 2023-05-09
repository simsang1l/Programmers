def solution(n, m, section):
    answer = 1
    start = section[0] # 덧칠할 시작점
    # 덧칠을 하면 section[idx] + m - 1 만큼 칠해진다.
    for idx in range(1, len(section)) :
        if section[idx] - start >= m:
            answer += 1
            start = section[idx]
        
    return answer