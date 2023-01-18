def solution(dots):
    answer = 0
    # 두 점을 잇는 경우 3가지
    # dots[0]dots[1], dots[2]dots[3]
    # dots[0]dots[2], dots[1]dots[3]
    # dots[0]dots[3], dots[1]dots[2]
    # 기울기 같으면 평행
    
    if (dots[1][0]-dots[0][0]) / (dots[1][1]-dots[0][1]) == (dots[3][0]-dots[2][0]) / (dots[3][1]-dots[2][1]):
        answer = 1
    elif (dots[2][0]-dots[0][0]) / (dots[2][1]-dots[0][1]) == (dots[3][0]-dots[1][0]) / (dots[3][1]-dots[1][1]):
        answer = 1
    elif (dots[3][0]-dots[0][0]) / (dots[3][1]-dots[0][1]) == (dots[2][0]-dots[1][0]) / (dots[2][1]-dots[1][1]):
        answer = 1
    
    
    return answer