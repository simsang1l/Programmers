def solution(rows, columns, queries):
    answer = []
    
    # rows x columns 크기의 행렬 초기화
    arr = [[j + i*columns for j in range(1, columns + 1)]for i in range(rows)]
    
    for x1, y1, x2, y2 in queries :
        x1, y1, x2, y2 = x1 - 1, y1-1, x2-1, y2-1
        temp = arr[x1][y1]
        min_val = temp

        for i in range(x1, x2):
            val = arr[i+1][y1]
            arr[i][y1] = val
            min_val = min(min_val, val)
        for i in range(y1, y2):
            val = arr[x2][i+1]
            arr[x2][i] = val
            min_val = min(min_val, val)
        for i in range(x2, x1, -1):
            val = arr[i-1][y2]
            arr[i][y2] = val
            min_val = min(min_val, val)
        for i in range(y2, y1, -1):
            val = arr[x1][i-1]
            arr[x1][i] = val
            min_val = min(min_val, val)
        
        arr[x1][y1+1] = temp
        answer.append(min_val)
        

    return answer

print(solution(6, 6, [[2, 2, 5,4], [3, 3, 6, 6], [5, 1, 6, 3]]))