def solution(numbers):
    answer = 0
    numbers.sort()
    
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    
    return answer

# 다른 사람 풀이
## lambda를 이용한 방법, 속도도 빠름
solution = lambda x: sum(range(10)) - sum(x)

## 문제 해결에 정말 잘 집중되어 있는 코드
def solution(numbers):
    return 45 - sum(numbers)