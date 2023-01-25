def solution(lines):
    answer = 0
    
    # 겹치는 수 찾아 개수 세기
    # 겹친다 정의 -> 2개 이상 배열에 값이 동시에 있다
    # 2개 이상 값이 있어도 길이를 잴땐 값이 -1이 되어 시작 점의 값 제외
        ## ex) 점 3, 4, 5 가 겹치면 길이는 2임
    # 점 2개 겹치는 경우 + 점 3개 겹치는 경우 = answer
    
    line_val = {}
    
    for i in lines:
        
        for j in range(i[0] + 1, i[1] + 1):
            
            if j not in line_val :
                line_val[j] = 1
            else :
                line_val[j] += 1
                
    for key, value in line_val.items():
        if value >= 2 :
            answer += 1
    
    return answer