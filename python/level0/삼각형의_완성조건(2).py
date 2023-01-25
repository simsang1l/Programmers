def solution(sides):
    answer = 0
    # c < a + b
    
    # a, b 중 하나가 가장 긴 변
    # c가 가장 긴 변
    sides.sort(reverse = True)
    start = sides[0] - sides[1] + 1
    
    for i in range(start, sides[0] + 1):
        if i < start + sides[1] :
            answer += 1
        else:
            break
    
    for i in range(sides[0] + 1, sides[0] + sides[1]):
        if i < sides[0] + sides[1]:
            answer += 1
        else :
            break
            
    return answer