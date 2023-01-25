# 꼭지점 좌표가 랜덤으로 나옴
# 좌표의 x, y값이 같다면 다음 점은 같을리가 없다

def solution(dots):
    answer = 0
    x = 0
    y = 0
    
    if dots[0][0] != dots[1][0]:
        x = abs(dots[1][0] - dots[0][0])
    else :
        x = abs(dots[2][0] - dots[0][0])
    
    if dots[0][1] != dots[1][1]:
        y = abs(dots[1][1] - dots[0][1])
    else :
        y = abs(dots[2][1] - dots[0][1])
        
    answer = x * y
    
    return answer