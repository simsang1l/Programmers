def solution(my_strings, parts):
    answer = ''
    for idx, (s, e) in enumerate(parts):
        answer += my_strings[idx][s:e+1]
    return answer


# 다른 사람 풀이
def solution(my_strings, parts):
    answer = ''
    for string, (s, e) in zip(my_strings, parts):
        answer += string[s:e+1]
    return answer