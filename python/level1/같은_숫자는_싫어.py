def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    
    for i in arr :
        if len(answer) == 0:
            answer.append(i)
        elif i != answer[-1]:
            answer.append(i)
            
            
    return answer


# 다른 사람 풀이 
def solution(arr):
    answer = []
    for item in arr:
        if answer[-1:] == [item]: continue # answer[-1:]같이 사용하면 맨 끝의 인덱스 값을 가져올 수 있음
        answer.append(item)
    return answer