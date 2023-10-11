def solution(my_string, indices):
    answer = ''
    my_lst = list(my_string)
    for i in indices:
        my_lst[i] = ''
    answer = ''.join(my_lst)
    return answer


# 다른 사람 풀이
# 리스트안의 값 지우기!
def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)