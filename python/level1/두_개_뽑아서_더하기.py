from itertools import combinations

def solution(numbers):
    answer = []
    
    for i, j in list(combinations(numbers, 2)):
        answer.append(i + j)
        
    answer = sorted(set(answer))
    
    return answer

def solution(numbers):
    answer = []
    length = len(numbers)
    a = set() # set은 중복제거를 해주고 sorted정렬 해준다, 근데 list로 바꾸면 정렬이 풀린다고함
    
    # 모든 경우 answer에 담기
    for i in range(length):
        for j in range(length) :
            if i != j :
                a.add(numbers[i] + numbers[j])
            
    answer = list(a)
    answer = sorted(answer)
    
    return answer

# 다른 사람 풀이 
## combinations없이 풀기!
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    return answer 