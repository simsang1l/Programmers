# greedy 방법을 이용하는 문제
# 숫자 자리수가 최대 1,000,000자리이기 때문에 combination을 사용하면 초과가 될 것 같음
# 제거만 가능하지 순서를 바꾸는건 아니기 때문에 stack을 이용하여 큰수를 넣고 자리수도 맞춰주는 방법 이용!
# 간단하지만 생각하기까지 시간이 꽤 걸리는구나..
def solution(number, k):
    answer = []
    
    for i in number :
        while k > 0 and answer and answer[-1] < i :
            answer.pop()
            k -= 1
        answer.append(i)
    
    answer = ''.join(answer[:len(answer) - k]) # 제거 횟수를 다 사용하지 않았을때 남은 횟수만큼 리스트 뒷부분을 잘라 주기


    return answer