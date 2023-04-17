def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1, count + 1) :
        total += price * i
        
    answer = 0 if total- money < 0 else total- money
    
    return answer

# 다른 사람 풀이
## 등차수열을 이용한 방법..
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

## 나의 풀이를 한줄로 표현한다면
def solution(price, money, count):
    return max(sum([price*i for i in range(1,count+1)]) - money,0)