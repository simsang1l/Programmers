import re

def solution(my_string):
    answer = 0
    result = re.sub(r'[^0-9]', '', my_string)

    for s in result:
        answer += int(s)
        
    
    return answer