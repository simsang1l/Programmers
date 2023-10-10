def solution(my_string, m, c):
    answer = ''
    lst = []
    for i in range(0, len(my_string), m):
        lst.append(my_string[i:i+m])
    
    for i in lst:
        answer += i[c-1]
        
    return answer