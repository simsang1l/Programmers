def solution(num, total):
    answer = []
    # num = 홀수
        # N개, mid, N개
    # num = 짝수
        # N개, mid, (N + 1)개

    mid = total // num # num = 홀수, 출력할 리스트의 가운데 있는 값
    N = (num - 1) // 2 
    start = mid - N
    
    while num != len(answer):
        answer.append(start)
        start += 1
    
    return answer