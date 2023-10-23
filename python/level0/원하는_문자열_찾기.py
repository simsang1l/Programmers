def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString :
        answer = 1
        
    return answer