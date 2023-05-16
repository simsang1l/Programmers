def solution(wallpaper):
    answer = []
    lst_x = []
    lst_y = []
    
    for x_idx, x in enumerate(wallpaper):
        for y_idx, y in enumerate(x) :
            if y == '#':
                lst_x.append(x_idx)
                lst_y.append(y_idx)
    answer = [min(lst_x), min(lst_y), max(lst_x) + 1, max(lst_y) + 1]
            
    return answer

# 다른 사람 풀이
# 2023.05.16 현재 비슷한 풀이가 많았다.