def solution(my_string):
    answer = 0
    
    # 숫자 연산자 숫자 연산자 순으로 입력된다고 가정해보고 시작
    
    my_string = my_string.split(' ')
    answer = int(my_string[0])
    
    for idx, value in enumerate(my_string):
        if value == '+':
            answer += int(my_string[idx + 1])
        elif value == '-':
            answer -= int(my_string[idx + 1])
            
    return answer