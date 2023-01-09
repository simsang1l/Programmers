def solution(my_string):
    answer = ''
    # 대문자를 소문자로 변경
    # 문자열 정렬
    
    s_lst = []
    
    for i in my_string:
        if i.isupper() is True:
            s_lst.append(i.lower())
        else:
            s_lst.append(i)
            
    s_lst.sort()
    
    for i in s_lst:
        answer += i
    
    return answer