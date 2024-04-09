# 재귀로 풀어야겠다는 생각으로 풀었다.
def solution(enroll, referral, seller, amount):
    answer = []
    result = {i: 0 for i in enroll}
    boss = {e: r for e, r in zip(enroll, referral)}

    def find_referee(employee, result, price):
        # 이건 질문을 참고하니 답이 나왔다.
        # 줄 돈이 없는데 계산하고 있는건 아닌가?라는 답변이었다.
        if price == 0 :
            return True
        # 추천인이 없다면 그냥 종료?
        if boss[employee] == '-':
            result[employee] -= price
        else :
            # 추천인에게 돈주기
            result[employee] -= price
            result[boss[employee]] += price
            
            # 추천인의 추천인이 있는지 찾기
            return find_referee(boss[employee], result, price//10)
    
    for s, a in zip(seller, amount) :
        a = a*100
        # 판매자가 판 금액
        result[s] += a
        
        find_referee(s, result, a//10)

    answer = list(result.values())
    
    return answer