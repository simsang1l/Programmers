def solution(s):
    answer = ''
    # 문자가 나온 횟수를 저장하는 dictionary 생성
    # 한번만 등장한 문자 출력 및 정렬
    cnt_string = {}
    string_lst = []
    
    for i in s :
        if i in cnt_string :
            cnt_string[i] += 1
        else :
            cnt_string[i] = 1

    for key, values in cnt_string.items() :
        if values == 1:
            string_lst.append(key)
    
    
    string_lst.sort()
    answer = ''.join(string_lst)
        
    return answer