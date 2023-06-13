# 테스트 16 실패
def solution(n):
    answer = 0
    for i in range(1, n):
        score = i
        for j in range(i + 1, n):
            if score > n :
                break
            elif score == n :
                answer += 1
                break
            else :
                score += j
            
    answer += 1 # n인 경우 추가
            
    return answer

# 수정코드
## 대표적으로 3일 때 문제가 발생함. --> 정답으로 2가 나와야 하는데, 비교한다음 더하기 때문에 정답으로 1이 나옴
## 비교한다음 더하는 과정이 아닌 더한다음 비교하는 과정을 거치면 해결된다.
def solution(n):
    answer = 0
    for i in range(1, n):
        score = i
        for j in range(i + 1, n):
            score += j 
            if score > n :
                break
            elif score == n :
                answer += 1
                break
            else :
                continue
            
            
    answer += 1 # n인 경우 추가
            
    return answer