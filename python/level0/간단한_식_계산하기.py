def solution(binomial):
    answer = 0
    lst = binomial.split(' ')
    answer = eval(f'{lst[0]} {lst[1]} {lst[2]}')
    
    return answer