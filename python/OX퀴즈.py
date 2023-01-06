def solution(quiz):
    answer = []
    
    
    # 식 추출
    for i in quiz:
        # 숫자와 연산 기호 추출
        value = i.split(' ')
        if value[1] == '+' and int(value[0]) + int(value[2]) == int(value[4]):
            answer.append('O')
        elif value[1] == '-' and int(value[0]) - int(value[2]) == int(value[4]):
            answer.append('O')
        else :
            answer.append('X')
        
        
    return answer