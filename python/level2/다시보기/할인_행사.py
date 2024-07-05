"""
하루에 1개 품목만 구매 가능하고 10일 연속으로 일치해야 함
number원소의 합이 10이고 want의 길이가 number의 길이와 같으므로 number가 더 큰 경우 고려할 필요 없음
할인하는 10개 품목의 개수가 같으면 회원가입 해도 되는 상황.
"""
def solution(want, number, discount):
    answer = 0
    dic = {w:n for w, n in zip(want, number)}
    
    for i in range(len(discount)):
        tmp = discount[i: i+10]
        check = {}
        
        for f in tmp:
            if f not in check:
                check[f] = 1
            else : 
                check[f] += 1
        
        if dic == check :
            answer += 1
            
    return answer