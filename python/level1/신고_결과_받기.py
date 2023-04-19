def solution(id_list, report, k):
    answer = []
    
    # 신고한 사람과 신고 당한사람 명단 {신고자: [신고당한사람]}
    mail = {}
    
    # 신고 당한 사람별 신고 횟수
    users = {}
    
    # 신고한 사람이 메일 받은 횟수
    mail_cnt = {}
    
    for userid in id_list:
        users[userid] = 0
        mail[userid] = []
        mail_cnt[userid] = 0
                
    for val in set(report):
        user, singo = val.split()
        users[singo] += 1
        
        if user in mail :
            mail[user].append(singo)
    
    for i, j in mail.items():
        for key, val in users.items() :
            if val >= k:
                if key in j:
                    mail_cnt[i] += 1 
                
    answer = list(mail_cnt.values())
    
    return answer

# 다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    
    for r in set(report):
        # reports에 user별 신고당한 횟수 저장
        reports[r.split()[1]] += 1
    
    for r in set(report):
        # user별 신고당한 횟수가 k이상이면
        if reports[r.split()[1]] >= k:
            # list.index(value) 이런식으로 인덱스 접근 가능
            answer[id_list.index(r.split()[0])] += 1
    
    return answer