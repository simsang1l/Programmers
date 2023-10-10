def solution(my_string, is_prefix):
    answer = 0
    string = ''
    for i in my_string:
        string += i
        if is_prefix == string :
            answer = 1 
            break
        
    return answer

# 다른 사람 풀이
# startswith, str or tuple형식으로 사용하면 되고 True, False값 return.
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))