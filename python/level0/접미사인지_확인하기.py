def solution(my_string, is_suffix):
    answer = 0
    lst = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in lst : 
        answer = 1
    return answer

# 다른 사람 풀이
# endswith 는 문자열로 끝나는지 확인해줌
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))