def solution(phone_number):
    answer = ''

    for idx, value in enumerate(str(phone_number)): 
        if idx >= len(str(phone_number)) - 4:
            answer += value
        else :
            answer += '*'
            
    return answer

## 다른사람 풀이
# 속도는 훨씬 빠르다..
def solution(phone_number):
    answer = ''

    answer = '*' * (len(phone_number) - 4) + (phone_number[-4:])
            
    return answer