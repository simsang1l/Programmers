def solution(absolutes, signs):
    answer = 0
    
    for i, j in zip(absolutes, signs):
        if j == False:
            i = i * (-1)
        answer += i
    
    return answer

# 다른사람 풀이
## comprehension 이용

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))