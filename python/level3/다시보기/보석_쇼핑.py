"""
카카오 테크 블로그 해설처럼 2개 포인터를 이용하는 방법
1. 인덱스를 저장하는 start, end 선언
2. 모든 종류의 보석을 포함하는 구간이 될 때 까지 end를 증가
3. 구간 중 가장 짧은 구간을 구하기 위해 start 인덱스를 증가하며 구간의 길이 줄여보기
4. 현재 구간이 조건을 만족하지 않으면 end인덱스를 증가하며 구간 탐색
5. 위 과정 반복
6. 구간을 전부 탐색했다면 탐색종료 및 조건을 만족하는 구간 중 길이가 가장 짧은 구간의 start, end 리턴
"""
from collections import defaultdict

def solution(gems):
    answer = [0, 0]
    
    candidates = []
    start, end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda: 0)
    
    while True:
        kind = len(gems_dict)
        if start == gems_len:
            break
        if kind == gem_kind :
            candidates.append((start, end))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        if end == gems_len:
            break
        if kind != gem_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue
        
    length = float('inf')
    for s, e in candidates:
        if length > e - s:
            length = e - s
            answer[0] = s+1
            answer[1] = e
            
    return answer


"""
정확성은 맞았지만 효율성 테스트는 모두 실패
"""
def solution(gems):
    answer = []
    # 모든 종류의 물품을 하나씩 구매한건지 어떻게 알까?
    length = len(set(gems))
    gem_length = len(gems)
    
    # 진열대 길이
    display_stand = 100001
    
    # 가장 짧은 구간을 구하는 방법?
    cnt_list = []
    # 1. index 0 부터 length만큼의 물품을 구매하는데 얼마나 걸리는지 저장. index 0번이 끝나면 index 1번 조사
    for i in range(gem_length) :
        cnt = 1
        tmp = set()
        tmp.add(gems[i])
        for k in range(i, gem_length):
            if gems[k] not in tmp :
                tmp.add(gems[k])
                cnt += 1
                
            if len(tmp) == length and (k-i+2) < display_stand:
                display_stand = k-i+2
                cnt_list.append([k - i, i+1, k+1])
                break
    cnt_list.sort(key = lambda x: (x[0], x[1]))

    answer = cnt_list[0][1:]
    
    return answer