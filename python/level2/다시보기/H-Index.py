# citations[i] == h번 인용된 논문
# len(citations) - i == h번 이하 인용된 논문의 수
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)) :
        if citations[i] >= len(citations) - i :
            answer += 1
        
    return answer


# 다른 풀이
"""
h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용되었을 때 이 학자의 H-index는 h로 정의
i + 1번째 논문이 i번 이하로 인용되었다는건
i + 1 편의 논문이 모두 i + 1번 이상 인용 되지 않았다는 것을 의미함.
즉 H-index는 최대 i일 수 있음.
"""
def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)
