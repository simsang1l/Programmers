def solution(myString):
    answer = ''
    std = ord('l')
    for i in myString :
        if ord(i) < std :
            answer += 'l'
        else :
            answer += i
        
    return answer