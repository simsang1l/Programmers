def solution(line):
    answer = []
    lst = [] # 교점 모음
    
    # 교점 찾기
    for i in range(len(line)) :
        a, b, e = line[i]
        for j in range(i+1, len(line)) :
            c, d, f = line[j]
            
            x_1, x_2 = b * f - e * d, a * d - b * c
            y_1, y_2 = e * c - a * f, a * d - b * c
            
            if x_2 == 0 :
                continue
            else :
                x, y = x_1 / x_2, y_1 / y_2
                if x.is_integer() and y.is_integer():
                    lst.append([int(x), int(y)])

    # 그려야하는 좌표 평면의 크기 구하기                
    max_x = lst[0][0]
    max_y = lst[0][1]
    min_x = lst[0][0]
    min_y = lst[0][1]

    for x, y in lst :
        if x > max_x :
            max_x = x
        if y > max_y :
            max_y = y
        if x < min_x :
            min_x = x
        if y < min_y :
            min_y = y

    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    # y축은 상하반전되어 있어 max_y - y
    for x, y in lst :
        answer[max_y - y][x - min_x] = '*'
        
    answer = [''.join(_) for _ in answer]
     
    return answer