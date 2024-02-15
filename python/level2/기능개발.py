"""
남은 일수를 계산하기 위해 남은 작업진도를 days에 저장
deploy하는날 완료된 기능들이 있는경우 count += 1 실행
deploy하는날 아직 완료되지 않은 기능이 있는경우 count를 answer에 insert
마지막 deploy날의 count를 넣어주기위해 while문 다음에 count 값을 insert함.
"""
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    
    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100 - progress) / speed))
    
    deploy_day = days.popleft()
    count = 1
    while days:
        if deploy_day >= days[0]:
            days.popleft()
            count += 1
        else:
            answer.append(count)
            deploy_day = days.popleft()
            count = 1
            
    answer.append(count)
    
    return answer

# 다른사람 풀이
"""
나와 동일한 생각이지만 더 쉽게 풀어낸 코드
1. math.ceil을 통해 올림 적용
2. index를 이용한 개수 값 구하기
3. 가장 마지막 배포를 고려한 for문 밖 append구문
"""
import math


def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(progresses) - front)  

    return answer


"""
생각은 했지만 구현은 못한 코드
시간을 이용하여 배포가 필요한 작업들에 모두 pop적용!
"""
def solution(progresses, speeds):
    
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer