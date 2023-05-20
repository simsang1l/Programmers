import re

def solution(str1, str2):
    answer = 0
    str1_dict = {}
    str2_dict = {}
    str_dict = {}
    
    new_str1 = [(str(str1[i]) + str(str1[i+1])).lower() for i in range(len(str1) - 1)]
    new_str2 = [(str(str2[i]) + str(str2[i+1])).lower() for i in range(len(str2) - 1)]
    
    # 숫자(\d), 공백(\s), 특수문자(\W) , 문제 1개 통과 실패
    # new_str1 = [val for val in new_str1 if not re.search(r'\d|\s|\W', val)]
    # new_str2 = [val for val in new_str2 if not re.search(r'\d|\s|\W', val)]
    new_str1 = [val for val in new_str1 if val.isalpha()]
    new_str2 = [val for val in new_str2 if val.isalpha()]
    
    
    for val in new_str1:
        if val in str1_dict:
            str1_dict[val] += 1
        else :
            str1_dict[val] = 1
            
    for val in new_str2:
        if val in str2_dict:
            str2_dict[val] += 1
        else :
            str2_dict[val] = 1
    
    for key, val in str1_dict.items():
        str_dict[key] = [val]
        
    for key, val in str2_dict.items():
        if key in str_dict :
            str_dict[key].append(val)
        else :
            str_dict[key] = [val]
            
    intersect_lst = []
    union_lst = []
    
    for key, val in str_dict.items():
        if len(val) == 2 :
            for i in range(min(val)):
                intersect_lst.append(key)
        for i in range(max(val)):
            union_lst.append(key)
    
    if len(union_lst) == 0:
        answer = 65536
    else :
        answer = int(len(intersect_lst) / len(union_lst) * 65536)
                
    return answer

# 다른 사람 풀이
## 교집합과 합집합을 구하는 방법 ...
from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)