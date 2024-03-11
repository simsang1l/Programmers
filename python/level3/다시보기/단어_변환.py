"""
문제는 풀었지만 BFS로 푸는 방법 다시 생각!
"""
def solution(begin, target, words):
    answer = 0
    
    if target in words:
        for word in words:
            cnt = 0
            t_cnt = 0
            
            # begin과 word의 한 글자씩 비교하기
            for b, w in zip(begin, word):
                if b != w :
                    cnt += 1
            if cnt == 1 :
                begin = word
                answer += 1
                
            # begin과 target을 한 글짜식 비교하여 한 글자 차이가 난다면 answer에 1을 더하고 loop끝내기
            for b, t in zip(begin, target):
                if b != t:
                    t_cnt += 1
            if t_cnt == 1:
                answer += 1
                break
            
    return answer

# 다른 사람 풀이
"""
단어가 변환되기 위해 알파벳 1개만 바뀔 수 있고, word안에 있는 단어로 변환이 가능함.
최소 단계를 찾아야 하니 BFS를 사용하면 될 것 같다.

1. words에 target이 없으면 바로 0 반환
2. 시작 단어부터 queue에 담는다. 단계는 0으로 초기화
2. 해당 단어가 words에 존재하는 단어중 1개의 알파벳 값만 다르면 큐에 넣어주고 반복
3. 만약 target값을 찾으면 지금까지 세어준 단계 반환
"""

from collections import deque

def can_transform(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))
                
    return 0
