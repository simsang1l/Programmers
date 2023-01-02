def solution(sides):
    answer = 0
    # 가장 긴 변 < 변1 + 변2
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else : 
        answer = 2
        
    return answer