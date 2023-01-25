# 평균값을 가지는 list 생성
# 평균 값을 가지면 동일한 순번 가진다

def solution(score):
    answer = []
    seq = []
    
    for i in score:
        seq.append(sum(i) / len(i))
    
    sort_score = sorted(seq, reverse = True)
    
    for i in seq :
        answer.append(sort_score.index(i) + 1)
        
    
    return answer