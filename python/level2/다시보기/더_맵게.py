# 테스트 16, 18, 22, 23, 효율성 테스트 실패
def solution(scoville, K):
    answer = 0
    
    while  len(scoville) >= 2 :
        
        a = scoville.pop(scoville.index(min(scoville)))  + scoville.pop(scoville.index(min(scoville))) * 2
                                                                     
        scoville.append(a)
        answer += 1
        
        if min(scoville) >= K :
            break
            
    if len(scoville) < 2 and answer < K:
        answer = -1
    
    return answer

## 힙(Heap)에 대한 공부가 필요할거 같다!

# 아직 알송달송...
# 다른 사람 풀이
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    now = scoville[0]

    while now < K and len(scoville) > 1:

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + second*2
        answer += 1
        heapq.heappush(scoville, new)
        now = scoville[0]

    if min(scoville) < K:
        answer = -1

    return answer