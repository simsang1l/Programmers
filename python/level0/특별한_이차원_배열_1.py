def solution(n):
    answer = []
    for i in range(n):
        lst = []
        for j in range(n):
            if i == j :
                lst.append(1)
            else :
                lst.append(0)
        answer.append(lst)
    return answer


# 다른 사람 풀이
# 모든 값을 0으로 만든후 1로 바꾸기
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer

# numpy를 이용하는 방법
import numpy as np

def solution(n):
    return np.eye(n).tolist()