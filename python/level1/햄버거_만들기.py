def solution(ingredient):
    answer = 0
    order = []
    
    for val in ingredient:
        order.append(val)
        if order[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                order.pop()
        
    return answer

def solution(ingredient):
    answer = 0
    order = []
    
    for val in ingredient:
        order.append(val)
        if order[-4:] == [1, 2, 3, 1]:
            answer += 1
            del order[-4:]
        
    return answer