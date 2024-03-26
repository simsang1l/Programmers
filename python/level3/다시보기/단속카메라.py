# 테스트케이스만 통과
# 반례: [[2, 2], [0, 1], [-10, 9]],  2
def solution(routes):
    answer = 0
    routes.sort()
    changed = 1
    
    for i, o in routes:
        if changed == 1 :
            in_point = i
            out_point = o
            changed = 0
            
        if i > in_point and o >= in_point :
            in_point = i
        
        if o < out_point :
            out_point = o
        
        if o > out_point or i > out_point:
            answer += 1
            changed = 1
        print(i, o, in_point, out_point)
            
        
    return answer