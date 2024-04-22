
# 다른 사람 풀이
# 1.철수행님이 먼저 토핑들을 전부 다 차지해버린다.
# 2.동생님이 뒤로 입장하여, 철수행님이 차지한 토핑들을 하나씩 뺏어버린다.
# 3.동생이 뺏을 때마다, 각자 가지고 있는 토핑의 종류가 같은지 확인한다.
# 4.같다면 답을 추가한다.
# 5.해시를 사용하면 시간이 아주 나이스하게 빨라진다.

def solution(topping):
    answer = 0

    forward = set()
    backward = {}
    for i in topping:
        backward[str(i)] = backward.get(str(i), 0) # dictionary.get('a', 'b') -> 딕셔너리에 'a'라는 key가 있으면 그 값을 가져오고 아니면 'a'라는 키에 'b'라는 값을 저장하라., 즉 초기화 방법중 하나!
        backward[str(i)] += 1
    for i in topping:
        forward.add(i)
        backward[str(i)] -= 1
        if backward[str(i)] == 0:
            del backward[str(i)]
        if len(forward) == len(backward.keys()):
            answer += 1
    return answer