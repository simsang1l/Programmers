"""
자료구조 heap: 우선순위의 개념을 큐에 도입한 자료 구조
heapq는 기본적으로 min heap(최소힙)으로 구성되어 있고
값들 중 가장 작은 값이 root에 위치하게 되고, heappop을 하게되면 root노드가 삭제됨.
(1, 2)와 같이 여러 값이 들어오면 첫 번째 요소를 기준으로, 첫번째 요소가 같다면 두번째 요소를 기준으로...
위치하게 된다.
"""
import heapq
def solution(jobs):
    jobs.sort() # 요청시간을 기준으로 오름차순 정렬
    num = len(jobs)
    waiting = [] # [소요시간, 요청시점], 현재 대기하고 있는 작업을 담은 리스트
    count = [] # 각 작업의 소요되는 시간
    now = 0 # 현재 시간

    while len(count) != num:
        while jobs and now >= jobs[0][0]:
            top = jobs.pop(0)
            heapq.heappush(waiting, (top[1], top[0]))
            print('in while;;', jobs, waiting, count, now)
            
        if jobs and waiting == []:
            top = jobs.pop(0)
            now = top[0]
            heapq.heappush(waiting, (top[1], top[0]))
        print('after if;;', jobs, waiting, count, now)
        
        x, y = heapq.heappop(waiting)
        now += x
        count.append(now - y)
        print('last;;', jobs, waiting, count, now)
        
    answer = sum(count) // num
    
    return answer


# 예제, 테스트 19, 20 만 통과 나머지는 모두 실패
# 순서대로 들어오는 경우와 예제를 간단히 풀이해 봄

def solution(jobs):
    answer = 0
    current_time = 0
    lead_time = 0
    
    jobs.sort(key = lambda x: x[0]+x[1])
    
    
    for idx, (s, e) in enumerate(jobs):
        wait_time = 0
        if s < current_time:
            wait_time = current_time - s
        lead_time += (wait_time + e)
        current_time += e
        
    answer = lead_time // len(jobs)
        
    return answer