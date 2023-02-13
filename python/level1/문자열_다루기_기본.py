import re

def solution(s):
    answer = True
    
    if (len(s) == 4 or len(s) == 6) and re.findall('[^0-9]+', s) == []:
        answer = True
    else :
        answer = False
        
    return answer

## 다른사람 풀이
