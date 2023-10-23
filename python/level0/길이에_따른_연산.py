def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    elif len(num_list) <= 10 :
        answer = 1
        for i in num_list:
            answer *= i
            
    return answer


# 다른 사람 풀이
# python스러운 풀이?
## eval(expression)
## 매개변수에 식을 문자열로 받아 파이썬이 실행해주는 것
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))


# prod라는 함수가 있다
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)