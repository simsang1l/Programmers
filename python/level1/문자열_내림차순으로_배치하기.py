# 대문자 먼저 정렬, 소문자 정렬하는듯
# sorted(s) = Zbcdefg
# sorted(s, reverse = True) = gfedcbZ

def solution(s):
    answer = ''
    answer = ''.join(sorted(s, reverse = True))
    return answer