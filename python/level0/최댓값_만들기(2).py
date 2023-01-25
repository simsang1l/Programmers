def solution(numbers):
    answer = 0
    # 음수 * 음수 일 때
    # 양수 * 양수 일 때
    
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        answer = numbers[0] * numbers[1]
    else :
        answer = numbers[-1] * numbers[-2]
    
    return answer