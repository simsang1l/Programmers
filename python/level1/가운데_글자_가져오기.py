def solution(s):
    answer = ''
    # 홀수라면 반으로 나누고 소수점 첫째자리에서 올림, 그 값
    # 짝수라면 반으로 나누고 소수점 첫째자리에서 버림, 그 값과 그 값 - 1값
    
    # math함수 안쓰고 올림 내림 방법
    
    ## Floor 
    ### floor = int(x)
    
    ## Ceiling
    ### ceiling = -int(-x)
    mid = len(s) / 2

    if len(s) % 2 != 0 :
        answer = s[int(mid)]
        # answer = s[math.floor(mid)]
    else :
        answer = s[-int(-mid) - 1] + s[-int(-mid)]
    
    return answer