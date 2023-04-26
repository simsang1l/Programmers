# 테스트 11 ~ 15 시간초과!
def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)

    while len(score) >= m:
        answer += min(score[:m]) * m
        del score[:m]
    
    return answer

## del을 하는 과정이 오래걸리는듯 ...
def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    # 현재 위치
    position = 0
    
    while len(score[position: position+m]) == m:
        answer += (min(score[position: position+m ]) * m)
        position += m
        
    return answer

# 다른 사람 풀이
## 나머지로 남는 건 어차피 포장을 못하는 상자로 버려질 것임.
## 단계별 첫번째 값은 최소값이고, m번씩 건너 뛰면서 합하기 때문에 정답임
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m