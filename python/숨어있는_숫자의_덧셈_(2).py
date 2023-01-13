import re
# 연속된 수를 하나의 숫자로 보는 방법

def solution(my_string):
    answer = 0
    
    # 문자끼리 나누기
    st = re.split('[a-zA-Z]', my_string)
    
    # 공백제거
    for i in st:
        if i.isnumeric() == True :
            answer += int(i)

    
    return answer