def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str) + 1, n):
        if i >= len(my_str) :
            break
            
        answer.append(my_str[i:i + n])

            
    return answer