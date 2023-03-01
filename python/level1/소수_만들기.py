## 직관적인 방법
def is_prime(n: int) -> bool:
    for i in range(2, n//2):
        if n % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    
    for first in range(len(nums)):
        for second in range(first+1, len(nums)):
            for third in range(second+1, len(nums)):
                if is_prime(nums[first] + nums[second] + nums[third]):
                    answer += 1
    
    return answer


## itertools를 이용하는 방법
import itertools

def is_primenum(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    
    for i in itertools.combinations(nums, 3):
        if is_primenum(sum(i)):
            answer += 1
    

    return answer