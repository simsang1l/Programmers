def solution(my_string, alp):
    answer = ''.join([i.upper() if alp == i else i for i in my_string])
        
    return answer