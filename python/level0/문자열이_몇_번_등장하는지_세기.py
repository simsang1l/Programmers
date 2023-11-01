def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i + len(pat)] == pat :
            answer += 1
        
    return answer


# 다른 사람 풀이
# startswith, endswith함수를 통해 특정 문자로 시작 혹은 끝날 때 True, False를 확인할 수 있음
# find나 rfind를 통해 찾을수도 있음 --> 처음 찾은 위치를 반환해줌
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer