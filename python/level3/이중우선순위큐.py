# 통과는 했지만 테스트케이스가 부실해서 그런 것 같다. 시간 복잡도 체크도 없고..
"""
1.  주어진 그대로 구현해보기
"""
def solution(operations):
    answer = []
    queue = []
    
    for i in operations:
        o, num = i.split(' ')
        num = int(num)
        if o == 'I':
            queue.append(num)
        elif o == 'D' and num == 1:
            if queue :
                queue.remove(max(queue))
        elif o == 'D' and num == -1:
            if queue :
                queue.remove(min(queue))
        
        
    if queue :
        answer = [max(queue), min(queue)]
    else :
        answer = [0, 0]
        
    return answer

# ChatGPT의 풀이
# 비슷해서 놀랐다
def solution(operations):
    queue = []
    
    for operation in operations:
        if operation.startswith("I"):
            # 삽입 명령어 처리
            num = int(operation.split()[1])
            queue.append(num)
        elif operation == "D 1":
            # 최댓값 삭제 명령어 처리
            if queue:
                queue.remove(max(queue))
        elif operation == "D -1":
            # 최솟값 삭제 명령어 처리
            if queue:
                queue.remove(min(queue))
    
    # 최종 결과 반환
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]
    
# heap을 이용한 방법도 알려줌
# 성능적인 면에서 입력 데이터의 크기가 크다면 heapq를 이용한 방법이 더 적합
import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    entry_finder = {}  # 유효한 항목을 추적하기 위한 딕셔너리
    counter = 0  # 고유 ID로 사용될 카운터

    for operation in operations:
        if operation.startswith("I"):
            # 삽입 명령어 처리
            num = int(operation.split()[1])
            heapq.heappush(min_heap, (num, counter))
            heapq.heappush(max_heap, (-num, counter))
            entry_finder[counter] = num
            counter += 1
        elif operation == "D 1":
            # 최댓값 삭제 명령어 처리
            while max_heap and max_heap[0][1] not in entry_finder:
                heapq.heappop(max_heap)
            if max_heap:
                _, idx = heapq.heappop(max_heap)
                del entry_finder[idx]
        elif operation == "D -1":
            # 최솟값 삭제 명령어 처리
            while min_heap and min_heap[0][1] not in entry_finder:
                heapq.heappop(min_heap)
            if min_heap:
                _, idx = heapq.heappop(min_heap)
                del entry_finder[idx]

    # 남은 유효한 값들 정리
    while min_heap and min_heap[0][1] not in entry_finder:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] not in entry_finder:
        heapq.heappop(max_heap)

    # 결과 반환
    if not entry_finder:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]