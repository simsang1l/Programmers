def solution(myString):
    answer = ''
    for i in myString:
        if i.lower() == 'a':
            answer += 'A'
        else :
            answer += i.lower()
            
    return answer

# 다른 사람 풀이
# replace를 활용할 수도 있겠군요
def solution(myString):
    return myString.lower().replace('a', 'A')