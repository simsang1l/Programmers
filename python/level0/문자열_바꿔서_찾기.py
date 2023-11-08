def solution(myString, pat):
    answer = 0
    newString = ''
    for i in myString:
        if i == 'B' :
            newString += 'A'
        elif i == 'A' :
            newString += 'B'
            
    if pat in newString:
        answer = 1
        
    return answer