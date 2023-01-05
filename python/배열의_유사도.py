def solution(s1, s2):
    answer = 0
    # 더 좋은 방법이 있으려나..?
    # 실간복잡도 = n**2 ??

    for i in s2:
        if i in s1 :
            answer += 1
            
    return answer