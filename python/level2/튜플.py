def solution(s):
    answer = []
    dic = {}
    tu = s.split('},')
    for i in tu :
        n = i.replace('{', '').replace('}','')
        n = n.split(',')
        
        dic[len(n)] = n
    dic = sorted(dic.items(), key = lambda x : x[0])
    
    for l, val in dic:
        for i in val:
            i = int(i)
            if i not in answer :
                answer.append(i)
            
    return answer

# 다른 사람 풀이
def solution(s):
    # 정규표현식을 통해 숫자만 추출
    # collections의 Counter는 각 원소가 몇 번씩 나오는지가 저장된 객체 얻을 수 있음
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter