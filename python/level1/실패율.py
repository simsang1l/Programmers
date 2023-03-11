def solution(N, stages):
    answer = []
    
    result = {}
    length = len(stages)
    for i in range(1, N+1):
        if length != 0 :
            count = stages.count(i)
            result[i] =  count/length
            length -= count
        else :
            result[i] = 0
    
    answer = sorted(result, key = lambda x : result[x], reverse = True)
    
            
    return answer
