def solution(n):
    x, y = -1, 0
    num = 1
    result = []
    
    # 배열 초기화
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    
    # 처음은 아래로 내려가기 때문에 n번 좌표 이동, 그 다음은 n-1번 좌표 이동, n-2번 좌표 이동... 
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: # 아래쪽으로 이동
                x += 1
            elif i % 3 == 1: # 오른쪽으로 이동
                y += 1
            else :      # 위쪽으로 이동
                x -= 1 
                y -= 1
            
            answer[x][y] = num
            num += 1
            
    for i in answer :
        for j in i :
            result.append(j)
            
    return result