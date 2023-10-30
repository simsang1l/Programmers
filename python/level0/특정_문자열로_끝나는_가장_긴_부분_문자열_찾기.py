def solution(myString, pat):
    answer = ''
    mylist = myString.split(pat)
    pat_count = len(mylist) - 1
    for i, value in enumerate(mylist):
        if pat_count != 0 :
            answer += value
            answer += pat
            pat_count -= 1
        elif pat_count <= 0 :
            break

    return answer

# 다른 사람 풀이
def solution(myString, pat):
    
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

# rfind, 오른쪽부터 해당하는 값이 시작하는 index를 찾음. 찾으면 종료인듯
def solution(myString, pat):
    
    return myString[0:myString.rfind(pat)] + pat
