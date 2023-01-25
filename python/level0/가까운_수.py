# 주어진 n과 차이가 가장 작은 경우 출력(음수가 주어지진 않기 때문에)

def solution(array, n):
    answer = 0
    difference = []
    
    
    for idx, num in enumerate(array) :
         difference.append([abs(num-n), num])
    
    # 오차, num기준으로 정렬
    answer = sorted(difference, key = lambda x: (x[0], x[1])) 
    
    return answer[0][1]