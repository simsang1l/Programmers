def solution(numbers):
    answer = ''
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, i in enumerate(num) :
        numbers = numbers.replace(i, str(idx))

    answer = int(numbers)
    
    return answer