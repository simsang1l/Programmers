"""
하루에 1개 품목만 구매 가능하고 10일 연속으로 일치해야 함
number원소의 합이 10이고 want의 길이가 number의 길이와 같으므로 number가 더 큰 경우 고려할 필요 없음
할인하는 10개 품목의 개수가 같으면 회원가입 해도 되는 상황.
"""
def solution(want, number, discount):
    answer = 0
    dic = {w:n for w, n in zip(want, number)}
    
    for i in range(len(discount)):
        tmp = discount[i: i+10]
        check = {}
        
        for f in tmp:
            if f not in check:
                check[f] = 1
            else : 
                check[f] += 1
        
        if dic == check :
            answer += 1
            
    return answer

# ChatGPT-4o의 수정
"""
1
"""
from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_count = Counter({w: n for w, n in zip(want, number)})
    current_count = Counter(discount[:10])

    # 초기 10일간의 할인 제품 상태 검사
    if all(current_count[w] >= want_count[w] for w in want_count):
        answer += 1

    # 슬라이딩 윈도우로 한 칸씩 이동하며 검사
    for i in range(10, len(discount)):
        # 윈도우의 오른쪽 끝 추가
        current_count[discount[i]] += 1
        # 윈도우의 왼쪽 끝 제거
        current_count[discount[i - 10]] -= 1
        if current_count[discount[i - 10]] == 0:
            del current_count[discount[i - 10]]

        # 현재 상태 검사
        if all(current_count[w] >= want_count[w] for w in want_count):
            answer += 1

    return answer