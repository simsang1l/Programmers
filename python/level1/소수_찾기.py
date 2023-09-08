# 테스트 11> 시간초과
# 효율성 테스트1, 2, 3, 4 > 시간초과
import math

def solution(n):
    answer = 0
    prime_num = []
    
    for i in range(2, n + 1):
        is_prime = 1
        for j in range(2, int(math.sqrt(i))+ 1) :
            if i % j == 0:
                is_prime = 0

        if is_prime == 1 :
            answer += 1       
    
    return answer


## 다른 사람 풀이 
### 1. 에라토스테네스의 체
#### n까지의 모든 소수를 구한다면, 2를 제외한 모든 2의 배수 제거,
#### 3을 제외한 모든 3의 배수 제거
#### 4는 2에서 제거
#### 5를 제외한 모든 5의 배수를 제거.... 반복

## 400ms이내에 모든 테스트 실행 완료
def solution(n):
    answer = 0
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            
    answer = len(num)
    
    return answer