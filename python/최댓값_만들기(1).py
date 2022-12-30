# 배열을 정렬한 후 최댓값 두개를 곱하면 되겠다

def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    
    return answer