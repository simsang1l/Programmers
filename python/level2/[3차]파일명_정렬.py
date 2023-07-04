"""
테스트 3, 4, 5, 12, 13, 14, 15 19, 20 실패
이유는?
    isdigit, isnumeric등의 함수로 head와 number를 나눌 때 오류가 있는듯
    abc123같이 파일명이 숫자로 끝나는 경우 number부분을 제대로 찾지 못함

    테스트 케이스
    입력 : ["O00321", "O49qcGPHuRLR5FEfoO00321"]
    기대값 : ["O00321", "O49qcGPHuRLR5FEfoO00321"]
    출력값 : ["O00321","O49500321qcGPHuRLRFEfoO"] --> 사라지고 출력되는 값들이 있는듯?

"""
def solution(files):
    lst = []
    for idx, i in enumerate(files):
        head = ''
        number = ''
        tail = ''
        
        for j in i :
            if number == '' and j.isdigit() == False :
                head += j
            elif head != '' and j.isdigit() == True:
                number += j
            else :
                tail += j
                
        lst.append([head, number,  tail])
    
    lst = sorted(lst, key = lambda item: (item[0].lower(), int(item[1])) )
    
    answer = [''.join(value) for value in lst]
            
    return answer

# 다른 사람의 풀이를 보고 비슷하게 접근했구나 느껴진다



# 다른 사람의 풀이
## 정규표현식이용하여 숫자로 나눔...
## 리스트도 정렬을 저렇게 할 수 있구나...
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]