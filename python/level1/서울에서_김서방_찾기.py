def solution(seoul):
    answer = ''
    
    for idx, value in enumerate(seoul):
        if value == 'Kim':
            kim = idx
            break
    
    answer = '김서방은 {}에 있다'.format(str(kim))
    return answer

## 다른사람 풀이
## list.index : list의 값 통해 값의 index를 알 수 있음.
def solution(seoul):
    answer = ''

    answer = '김서방은 {}에 있다'.format(str(seoul.index('Kim')))
    
    return answer