def solution(chicken):
    answer = 0
    # 쿠폰수 = 치킨수
    while chicken >= 10 :
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div + mod
    
    return answer