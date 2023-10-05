def solution(my_string, n):
    answer = ''
    
    answer = my_string[::-1][:n][::-1]
    return answer

# 다른 사람 풀이
def solution(my_string, n):
    return my_string[-n:]