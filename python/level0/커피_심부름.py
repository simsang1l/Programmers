def solution(order):
    answer = 0
    for i in order :
        if 'americano'in i  or 'anything' in i:
            answer += 4500
        elif 'cafelatte' in i:
            answer += 5000
    return answer