def solution(myString):
    answer = ''
    for i in myString:
        if i.isupper() :
            answer += (i.lower())
        else :
            answer += i
    return answer