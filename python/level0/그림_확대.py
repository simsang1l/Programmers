"""
예를 들어 2배확대한다면
문자열 하나가 열 방향으로 2배 늘어남
한줄이 행 방향으로 2배 늘어남
"""

def solution(picture, k):
    answer = []
    for i in picture :
        value = ''
        for j in i :
            value += (j*k)
        for s in range(k) :
            answer.append(value)
        
    return answer