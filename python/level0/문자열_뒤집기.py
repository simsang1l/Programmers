def solution(my_string, s, e):
    answer = ''
    my_lst = list(my_string)

    if s - 1 < 0 :
        my_lst[s:e+1] = my_lst[e::-1]
    else :
        my_lst[s:e+1] = my_lst[e:s-1:-1]
        
    answer = ''.join(my_lst)
    
    return answer

# 다른 사람 풀이
def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]