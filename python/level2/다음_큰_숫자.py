# 1씩 더해서 1의 개수가 맞을 때 까지 찾아가는 방법
def solution(land):
    answer = 0
    
    # 1개수 세기
    cnt = list(bin(land).replace('0b', '')).count('1')
    
    while land :
        land += 1
        result_cnt = list(bin(land).replace('0b', '')).count('1')
        
        if cnt == result_cnt :
            break
    answer = land 
    
    return answer