def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for n, y in zip(name, yearning):
        score[n] = y
    
    for i in photo :
        result = 0
        for name in i :
            if name in score :
                result += score[name]
        answer.append(result)
        
    return answer

# 다른 사람 풀이
## index접근하는 방법
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]