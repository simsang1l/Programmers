def solution(n):
    answer = 0

    for i in str(n) :
        answer += int(i)

    return answer

# 다른 사람 풀이 
## map 함수
### 리스트의 요소를 지정된 함수로 처리해주는 함수
### map(함수, 리스트)
### 값을 보기위해선 list(map(함수, 리스트))처럼 사용

def solution(n):
    answer = 0

    answer = sum((list(map(int, str(n)))))

    return answer