def solution(start, end_num):
    answer = [i for i in range(start, end_num-1, -1)]
    return answer


# 다른 사람 풀이
# 이런 간단한 방법이..!
def solution(start, end):
    return list(range(start,end-1,-1))