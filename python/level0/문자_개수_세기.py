def solution(my_string):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = 0
    for i in range(26):
        dic[chr(65+i).lower()] = 0
        
    for i in my_string:
        dic[i] += 1
    answer = list(dic.values())
    return answer