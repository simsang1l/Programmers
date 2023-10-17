def solution(str_list):
    answer = []
    if 'l' in str_list:
        l_index = str_list.index('l')
    else :
        l_index = 20
    if 'r' in str_list:
        r_index = str_list.index('r')
    else :
        r_index = 20
    
    if l_index < r_index :
        answer = str_list[:l_index]
    else :
        answer = str_list[r_index+1:]
    
    return answer

# 다른 사람 풀이
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []
