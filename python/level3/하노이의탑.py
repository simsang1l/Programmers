"""
아이디어

시작기둥, 보조기둥, 대상 기둥이라고 하고 대상기둥에 원판을 모두 옮겨야 하는 상황임.

1. 가장 아래의 원판을 제외하고 나머지를 보조 기둥에 옮긴다.
2. 가장 아래 원판을 대상 기둥에 옮긴다.
3. 보조 기둥에 있는 원판을 대상 기둥에 옮긴다.

def hanoi(원판개수, 시작기둥, 보조기둥, 대상기둥):
    if 원판개수 == 1 :
        이동 from 시작기둥 to 대상기둥
    
    if 원판이 2개 이상:
        # 가장 아래 원판 제외하고 나머지를 시작기둥에서 보조 기둥으로 이동
        hanoi(원판 - 1, 시작기둥에서 보조기둥으로 대상기둥을 활용하서)
        이동 from 시작기둥 to 대상기둥
        # 보조 기둥에 있는 원판을 대상 기둥으로 이동
        hanoi(원판 - 1, 보조기둥에서 대상기둥으로 시작기둥을 활용해서)

"""

def hanoi(n, a, c, b, answer): # 원판개수, 시작기둥, 대상기둥, 보조기둥
    if n == 1 :
        answer.append([a, c])
    else:
        hanoi(n - 1, a, b, c, answer)
        answer.append([a, c])
        hanoi(n - 1, b, c, a, answer)
        
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer