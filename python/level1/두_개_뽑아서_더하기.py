from itertools import combinations

def solution(numbers):
    answer = []
    
    for i, j in list(combinations(numbers, 2)):
        answer.append(i + j)
        
    answer = sorted(set(answer))
    
    return answer

# 다른사람 풀이
## combinations없이 풀기!
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    return answer 