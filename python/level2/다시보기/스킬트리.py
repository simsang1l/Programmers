"""
테스트 2, 3, 4, 12만 통과
"""
def solution(skill, skill_trees):
    answer = 0
    skill_dict = {v:i for i, v in enumerate(skill)}
    
    for trees in skill_trees:
        state = 0
        step = 0  
        print(trees)
        for i in trees:
            print(i, step, state)    
            if i in skill_dict :
                if step == skill_dict[i]:
                    step += 1
                    state = 1
                # 선행 스킬 순서가 아닌 경우
                elif  step != skill_dict[i]:
                    state = 0
                    print('elif;;', i, step, state)
                    break
        if state == 1 :
            answer += 1
            
    return answer

# 다른 사람 풀이
def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = ""                      # 하나의 스킬트리를 뽑을 때마다 s 초기화
        for ch in skill_tree:       
            if ch in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
                s += ch
        if skill[:len(s)] == s:     # 만든 s를 기준으로 skill과 같다면 count += 1
            count += 1
    
    return count