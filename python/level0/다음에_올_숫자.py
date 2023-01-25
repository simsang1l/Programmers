# else에서 사용할 변수를 else 바깥에서 사용하면 
# 사용하지 않을 때도 계산을 해서 메모리 낭비하는게 있는가보다

def solution(common):
    answer = 0
    num = common[1] - common[0]
    
    if common[1] + num == common[2]:
        answer = common[-1] + num
    else :
        x = common[1] / common[0]
        answer = common[-1] * x
        
    return answer