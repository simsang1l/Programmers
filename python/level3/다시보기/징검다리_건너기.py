"""
아직 이해가 잘 안된다 다시 보자
"""

def solution(stones, k):
    answer = 0
    l, r = 1, max(stones)
    
    while l <= r :
        ct = 0
        mid = (l + r) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                ct += 1
            else :
                ct = 0
            if ct >= k :
                break
            
        if ct < k:
            l = mid + 1
        else:
            answer = mid
            r = mid - 1

    
    return answer