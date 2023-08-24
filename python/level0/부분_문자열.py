def solution(str1, str2):
    answer = 0
    
    if str1 in str2 :
        answer = 1
        
    return answer

def solution(str1, str2):
    answer = 0
    str2_copy = list(str2)
    
    for i in str2 :
        if str2_copy[:len(str1)] == list(str1):
            return 1
        str2_copy.pop(0)
        
    return answer