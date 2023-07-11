from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 경과시간
    answer = 1
    # 대기트럭
    standby_truck = deque(truck_weights)
    # 다리를 건너는 트럭
    move = []
    # 다리를 지난 트럭
    complete = []
    # 시작시간
    start_time = [] 

    while True:
        if start_time and answer - start_time[0] == bridge_length:
            complete.append(move.pop(0))
            start_time.pop(0)

        if standby_truck and sum(move) + standby_truck[0] <= weight:
            move.append(standby_truck.popleft())
            start_time.append(answer)

        if not start_time :
            break

        answer += 1

    return answer