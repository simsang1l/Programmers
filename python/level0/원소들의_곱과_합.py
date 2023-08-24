def solution(num_list):
    answer = 0
    
    mul = 1
    # 모든 원소들의 곱
    for i in num_list:
        mul *= i
    
    # 모든 원소들의 합의 제곱
    square = sum(num_list)**2
    
    if mul < square : 
        answer = 1
        
    return answer