def solution(x1, x2, x3, x4):
    answer = True
    answer = (x1|x2) & (x3|x4)
    return answer