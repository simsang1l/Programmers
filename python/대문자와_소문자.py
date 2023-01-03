# 1. 대소문자 구분
## isupper() --> 대문자인지 소문자인지 확인
# 2. 대소문자 변경

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper() is True:
           answer += i.lower() 
        else :
            answer += i.upper()
            
    return answer