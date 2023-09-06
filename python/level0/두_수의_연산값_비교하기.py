def solution(a, b):
    answer = 0
    if int(str(a) + str(b)) > 2 * a * b:
        answer = int(str(a) + str(b))
    else :
        answer = 2 * a * b
    return answer

# 다른사람풀이
def solution(a, b):
    answer = max(int(str(a)+str(b)), 2 * a * b)
    return answer