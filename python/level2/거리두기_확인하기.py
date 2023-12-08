def check(place):
    # P 값의 좌표만 p_list에 추가
    p_lst = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']
    
    for y, x in p_lst:
        for y2, x2 in p_lst:
            dist = abs(y - y2) + abs(x - x2)
            # 같은 좌표이거나 거리가 2 이상이면 넘어가기
            if dist == 0 or dist > 2 :
                continue
            # 거리가 1인 경우
            if dist == 1 :
                return 0 
            elif y == y2 and place[y][(x+x2)//2] != 'X': # 열이 같고 두 사람 사이 파티션이 없는 경우
                print('elif1', y, x, y2, x2)
                return 0
            elif x == x2 and place[(y+y2)//2][x] != 'X': # 행이 같고 두 사람 사이에 파티션 없는 경우
                print('elif2', y, x, y2, x2)
                return 0
            elif y != y2 and x != x2: # 열/행이 다른경우(대각선), 두 사람 사이 파티션이 없는경우
                if place[y2][x] != 'X' or place[y][x2] != 'X':
                    return 0
    return 1

def solution(places):
    answer = []
    
    for place in places :
        answer.append(check(place))

        
    return answer