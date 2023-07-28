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
