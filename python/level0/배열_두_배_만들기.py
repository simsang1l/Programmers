def solution(numbers):
    answer = []
    # ver1 루프를 통해 각 원소를 2배한 값을 answer에 담기 
    ## --> numbers가 너무 많아지면 오래걸리지 않을까?
    '''
    for num in numbers : 
        answer.append(num * 2 )
    '''
    
    # 다른 사람 풀이
    ## 표현 방식의 차이인것 같다. 속도 차이는 거의 없지 않나?
    ## answer = [num * 2 for num in numbers]
    
    
    return answer