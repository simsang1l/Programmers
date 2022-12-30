# my_string에 있는 숫자만 추출
## re라이블러리를 통해 숫자 제외하고 추출

# 추출한 숫자 오름차순 정렬

import re

def solution(my_string):
    answer = []
    result = re.sub(r'[^0-9]', '', my_string)

    for s in result:
        answer.append(int(s))
        
    answer.sort()
    
    return answer