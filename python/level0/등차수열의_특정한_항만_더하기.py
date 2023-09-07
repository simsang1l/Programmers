def solution(a, d, included):
    answer = 0
     
    for i in range(len(included)):
        if included[i] :
            answer += a

        a += d
        
    return answer

# 다른 사람 풀이 
#  d*index를 이용하면 몇번을 더해야 하는지 계산 가능!
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]==True:
            answer+=a+i*d
    return answer