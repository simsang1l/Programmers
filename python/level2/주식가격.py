# 효율성 테스트 시간초과
def solution(prices):
    answer = []
    
    while prices :
        price = prices.pop(0)
        time = 0
        for i in prices:
            time += 1
            if price > i :
                break
        answer.append(time)
        
    
    return answer

# collections의 deque를 이용하면 효율성 테스트도 통과!!
# pop(0)는 복잡도가 O(n) deque를 이용하면 O(1)이 된다고함. 왜?
# pop은 list의 길이만큼 오래 걸린다고 한다. deque는 인덱스 접근을 이용하여 O(1)만큼 걸린다고 함....
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices :
        price = prices.popleft()
        time = 0
        for i in prices:
            time += 1
            if price > i :
                break
        answer.append(time)
        
    
    return answer

# 다른 사람 풀이
# deque가 더 빠르지만 굳이 stack, queue를 이용하지 않아도 ~
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
