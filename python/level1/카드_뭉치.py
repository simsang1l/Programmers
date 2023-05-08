def solution(cards1, cards2, goal):
    answer = ''
    goal_lst = []
    
    for i in goal:
        if len(cards1) != 0 and cards1[0] == i :
            goal_lst.append(cards1.pop(0))
        elif len(cards2) != 0 and cards2[0] == i :
            goal_lst.append(cards2.pop(0))
        else :
            break
    
    if goal_lst == goal :
        answer = 'Yes'
    else :
        answer = 'No'
        
    return answer

# 다른 사람 풀이
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"