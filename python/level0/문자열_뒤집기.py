def solution(my_string):
    answer = ''
    ## slice로 문자열 뒤집기
    ## slice [start:stop:step], string[::-1]을 사용하면 반대 방향으로 리스트를 자를 수 있음
    answer = my_string[::-1]
    
    ## reversed로 뒤집기
    #answer = "".join(reversed(my_string))
    
    ## loop로 뒤집기
    '''
    for i in my_string:
        print('i;;',i)
        print('a;;',answer)
        answer = i + answer
    '''
    
    return answer