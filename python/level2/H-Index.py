# citations[i] == h번 인용된 논문
# len(citations) - i == h번 이하 인용된 논문의 수
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)) :
        if citations[i] >= len(citations) - i :
            answer += 1
        
    return answer