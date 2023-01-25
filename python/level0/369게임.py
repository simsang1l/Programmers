# 3, 6, 9의 개수 출력
# 문자로 변환한 후 하나씩 확인하여 개수 확인

def solution(order):
    answer = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            answer += 1
            
    return answer