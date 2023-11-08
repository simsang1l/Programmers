def solution(myString):
    answer = []
    lst = myString.split('x')
    for i in lst:
        answer.append(len(i))
    
    return answer