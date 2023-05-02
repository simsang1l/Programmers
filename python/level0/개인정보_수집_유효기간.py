from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    period = {}
    today = datetime.strptime(today, '%Y.%m.%d')
    
    for val in terms :
        k, p = val.split(' ')
        period[k] = int(p)
    
    for idx, val in enumerate(privacies):
        date, kind = val.split(' ')
        date = datetime.strptime(date, '%Y.%m.%d')
        
        if today >= date + relativedelta(months = period[kind]):
            answer.append(idx + 1)
    
    return answer

# 다른 사람 풀이
## datetime 없이 풀어보기
def solution(today, terms, privacies):
    answer = []
    # 조건상 날짜는 28일보다 클 수 없으므로 딕셔너리에 보호 일수 저장
    dic_terms = {t.split(" ")[0]:int(t.split(" ")[1])*28 for t in terms}
    # 날짜 연산을 쉽게 하기 위해 날짜를 총 일수로 변환
    today_val = 12*28*int(today.split(".")[0]) + 28 * int(today.split(".")[1]) + \
                int(today.split(".")[2])
    
    # 일수 계산으로 차이보다 작거나 같으면 answer에 저장
    for i,p in enumerate(privacies):
        gap = dic_terms[p[-1]]
        p = p[:-2]
        p_val = 12*28*int(p.split(".")[0]) + 28 * int(p.split(".")[1]) + \
                int(p.split(".")[2])
        if today_val - p_val >= gap:
            answer.append(i+1)
    
    return answer