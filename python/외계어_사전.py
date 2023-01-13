def solution(spell, dic):
    answer = 0
    
    
    for i in dic :
        classification = 0
        
        for j in spell :
            if j in i :
                classification += 1
                
        # spell을 다 쓰지 않은 경우 때문에 len(spell) <= len(i) 조건 추가
        if len(spell) <= len(i) and classification == len(i):
            answer = 1
            break
        else :
            answer = 2
            
    return answer