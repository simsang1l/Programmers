# 테스트 5 ~ 12, 14 실패
def solution(answers):
    answer = []
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = {}
    
    for idx, ans in enumerate(answers):
        if ans == math_1[idx % len(math_1)]:
            if 1 not in score.keys():
                score[1] = 1
            score[1] += 1
        if ans == math_2[idx % len(math_2)]:
            if 2 not in score.keys():
                score[2] = 1
            score[2] += 1
        if ans == math_3[idx % len(math_3)]:
            if 3 not in score.keys():
                score[3] = 1
            score[3] += 1
    sorted_score = sorted(score.items(), key = lambda value: (value[1], value[0]))
    
    for key, value in sorted_score:
        answer.append(key)
    
    return answer


##  다른 사람 풀이 
def solution(answers):
    answer = []
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        if ans == math_1[idx % len(math_1)]:
            score[0] += 1
        if ans == math_2[idx % len(math_2)]:
            score[1] += 1
        if ans == math_3[idx % len(math_3)]:
            score[2] += 1
    
    for idx, val in enumerate(score):
        if val == max(score):
            answer.append(idx + 1)
    
    return answer