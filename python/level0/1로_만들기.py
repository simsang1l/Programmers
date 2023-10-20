def solution(num_list):
    answer = 0
    idx = 0
    
    while sum(num_list) != len(num_list):
        if num_list[idx] != 1 :
            if num_list[idx] % 2 == 0:
                num_list[idx] = num_list[idx] // 2
            else :
                num_list[idx] = (num_list[idx] - 1)//2
            
            answer += 1
            
        else :
            idx += 1

    return answer


# 다른 사람 풀이
## 몫만 구하는 거라면 굳이 1을 빼고 나눌 필요가 없다!
def solution(num_list):
    answer = 0

    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1

    return answer