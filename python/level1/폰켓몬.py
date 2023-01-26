def solution(nums):
    answer = 0
    s = len(set(nums))
    n = len(nums)

    if s == n or s > n//2 :
        answer = n // 2
    else :
        answer = s
        
    return answer