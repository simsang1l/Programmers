def solution(my_string):
    answer = []
    my_string = my_string.split(' ')
    for i in my_string:
        if i == '':
            continue
        else :
            answer.append(i)
            
    return answer


# 다른 사람 풀이
# 문자열 혹은 공백 지우기 -> strip
def solution(my_string):
    my_string = my_string.strip()
    words = my_string.split()
    return words