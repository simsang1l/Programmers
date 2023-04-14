# 큰 문자열을 합칠때는 join() 매서드를 사용하는게 더 효율적이라고 한다.
# + 연산자는 불변(immutable)객체로 처리하여 각 + 연산마다 새로운 문자열을 생성한다고 한다
# 이로 인해 메모리 사용량과 성능에 영향을 미칠 수 있다고 함
def solution(food):
    answer = ''
    food_lst = ''
    for idx, i in enumerate(food[1:]):
        food_lst += str(idx+1) * (i//2)

    # answer = food_lst + '0' + food_lst[::-1]
    answer = ''.join([food_lst, '0', food_lst[::-1]])
    
    return answer