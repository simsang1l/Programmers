def solution(price):
    answer = 0
    
    # 10만원 이상 5% 할인
    # 30만원 이상 10% 할인
    # 50만원 이상 20% 할인
    ## price를 100으로 나누고 할인율을 적용하면 테스트 1개 통과 못함...

    if 100000 <= (price) < 300000:
        answer = int((price) * ((100 - 5) / 100))
    elif 300000 <= (price) < 500000:
        answer = int((price) * ((100 - 10) / 100))
    elif 500000 <= (price):
        answer = int((price) * ((100 - 20) / 100))
    else :
        answer = int(price)
        
    return answer