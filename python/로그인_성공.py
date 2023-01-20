def solution(id_pw, db):
    answer = ''
    

    for id_, pw in db :    
        
        if id_pw[0] == id_:
            if id_pw[1] == pw:
                answer = 'login'
            else :
                answer = 'wrong pw'
                
    if answer == '':
        answer = 'fail'
        
    return answer