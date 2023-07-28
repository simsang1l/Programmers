# priorities, index에 대한 queue를 이용
from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    index_queue = deque([i for i in range(len(priorities))])
    while priorities :
        print(priorities[0])
        first = priorities.popleft()
        index = index_queue.popleft()
        if list(filter((lambda x: x > first), priorities)) :
            priorities.append(first)
            index_queue.append(index)
        else :
            # 프로세스 실행완료
            answer += 1
            if location == index:
                break

    return answer

# 다른 사람 풀이
# filter쓸 필요 없이 any를 이용하여 조건 비교!
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer