# banned_id 형태가 완성되는 경우의 수 구하기
# *****같은건 자리수로 파악 가능
# fr*d* 같은건 어떻게 파악?
    # 한 글자씩? 3중 for문
from itertools import product

def solution(user_id, banned_id):
    answer = 0
    dic = {}
    
    for idx in range(len(banned_id)) :
        ban_user = banned_id[idx]
        # 딕셔너리 초기화
        dic[idx] = []
        
        for user in user_id:
            if len(ban_user) == len(user):
                state = 0
                for i in range(len(ban_user)):
                    if ban_user[i] == user[i] or ban_user[i] == '*':
                        state = 1
                    else :
                        state = 0
                        break
                if state == 1 :
                    dic[idx].append(user)
                
    lst = [value for value in dic.values()]
    
    # 유효한 조합만 필터링하고 중복 제거
    valid_combinations = set()
    all_combinations = product(*lst)
    
    for combination in all_combinations:
        if len(set(combination)) == len(banned_id):
            valid_combinations.add(tuple(sorted(combination)))
    
    answer = len(valid_combinations)
    
    return answer
