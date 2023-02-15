import re

def solution(s):
    answer = True
    
    if len(s) in (4, 6) and re.findall('[^0-9]+', s) == []:
        answer = True
    else :
        answer = False
        
    return answer

## 다른사람 풀이
### isdigit이란 함수도 있네요
def solution(s):
    answer = s.isdigit() and len(s) in (4, 6)

    return answer