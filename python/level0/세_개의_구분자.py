def solution(myStr):
    answer = []
    lst = myStr.replace('b', 'a').replace('c', 'a').split("a")
    for i in lst:
        if i :
            answer.append(i)
    if len(answer) == 0:
        answer = ["EMPTY"]
    
    return answer