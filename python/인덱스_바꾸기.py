def solution(my_string, num1, num2):
    answer = ''
    # 문자열을 변환할 수 없으므로 리스트로 변경하여 값 변경
    lst = list(my_string)
    
    num1_string = lst[num1]
    num2_string = lst[num2]
    lst[num2] = num1_string
    lst[num1] = num2_string
    
    answer = ''.join(lst)
    
    return answer