"""
효율성 테스트만 실패...
"""

def solution(info, query):
    answer = []
    for q in query:
        s = q.replace('and ', '').split(' ') # query의 항목
        cnt = 0
        
        for i in info :
            state = 0
            t = i.split(' ') # info의 항목

            for idx in range(len(t)) :
                
                if s[idx] == '-' or t[idx] == '-':
                    state = 1
                elif s[idx] == t[idx]:
                    state = 1
                elif idx == 4 and int(t[idx]) >= int(s[idx]):
                    state = 1
                else :
                    state = 0
                    break

            if state == 1:
                cnt += 1
        
        answer.append(cnt)
        
    return answer