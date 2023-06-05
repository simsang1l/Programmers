def hanoi(n, source, target, auxiliary, answer):
    if n > 0:
        # 원반 n-1개를 보조 기둥으로 이동(source->auxiliary)
        hanoi(n-1, source, auxiliary, target, answer)

        answer.append([source, target])

        # 원반 n-1개를 목표 기둥으로 이동(auxiliary->target)
        hanoi(n-1, auxiliary, target, source, answer)

        
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    
    return answer