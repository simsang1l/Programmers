def solution(myString):
    answer = []
    lst = myString.split('x')
    answer = sorted([i for i in lst if i])
    
    return answer