# 테스트 7~16번 실패
## n은 2000이하의 정수인데 2000을 테스트케이스로 넣어보면 오버플로우 문제라고 한다
def factorial(n):
    val = 1
    if n in (0, 1):
        return val
    else :
        for i in range(1, n+1):
            val *= i
        
    return val

def solution(n):
    answer = 0
    # 2칸을 멀리뛰기를 할 수 있는 최대 횟수
    step_2 = n//2
    
    # 같은값이 있을 때 순열을 이용 (예: aaabb라면 5!/(3!*2!)이렇게 계산할 수 있음 )
    for i in range(step_2+1):
        step_1 = n - (i*2)
        val = factorial(i+step_1)/(factorial(i)*factorial(step_1))
        answer += val
    
    answer = answer % 1234567
    
    return answer

# / 는 float형 반환, //는 int형 반환
# int는 32비트(-2147483684 ~ 2147483647), float는 64비트(15자리까지 표현 가능)

def factorial(n):
    val = 1
    if n in (0, 1):
        return val
    else :
        for i in range(1, n+1):
            val *= i
        
    return val

def solution(n):
    answer = 0
    k = 1234567
    # 2칸을 멀리뛰기를 할 수 있는 최대 횟수
    step_2 = n//2
    
    for i in range(step_2+1):
        step_1 = n - (i*2)
        val = factorial(i+step_1)//(factorial(i)*factorial(step_1))
        answer += int(val)
    
    answer = answer % k
    
    return answer