# 가로, 세로, 높이에 다 들어가 있으면된다.
# 가로/n * 세로/n * 높이/n = 상자에 들어갈 수 있는 주사위 최대 개수

def solution(box, n):
    answer = 0
    
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    
    return answer