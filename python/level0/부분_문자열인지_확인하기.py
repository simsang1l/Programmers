def solution(my_string, target):
    answer = 0
    
    if target in my_string:
        answer = 1
    
    return answer

# 앞에서부터 비교하면서 찾기
def solution(my_string, target):
    answer = 0

    my_string2 = list(my_string)

    for i in range(len(my_string)):
        if my_string2[:len(target)] == list(target):
            return 1
        my_string2.pop(0)

    return answer