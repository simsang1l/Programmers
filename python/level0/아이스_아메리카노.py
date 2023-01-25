def solution(money):
    answer = []
    cup_of_coffee = money//5500
    change = money - (5500 * cup_of_coffee)
    
    answer.append(cup_of_coffee)
    answer.append(change)
    
    return answer