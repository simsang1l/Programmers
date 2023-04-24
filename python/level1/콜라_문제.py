def solution(a, b, n):
    answer = 0
    
    while n >= a :
        remain = n % a
        n = n // a * b
        answer += n
        n += remain
        
    return answer

# 다른 사람 풀이
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b