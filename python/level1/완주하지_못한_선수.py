# 효율성 테스트에서는 상당히 떨어지는 성능
def solution(participant, completion):
    answer = ''
    # participant, completion 정렬
    # 완주를 못한 이름부터 다르기 시작
    participant.sort()
    completion.sort()
    # list 사이즈 맞춰주기위해 임의로 값 넣기
    completion.append('<end>')
    for idx, value in enumerate(participant):
        if value != completion[idx]:
            answer = value
            break
            
    return answer

## 다른 사람 풀이 
### hash는 같은 문자에 대해 같은 값을 가지게 됨
### 남은 hash값을 알면 그 문자에 대해 알 수 있음을 이용

def solution(participant, completion):
    answer = ''
    hashdict = {}
    sumHash = 0
    
    for part in participant:
        hashdict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    answer = hashdict[sumHash]
    
    
    return answer
