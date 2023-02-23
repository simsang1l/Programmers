def solution(num):
    answer = ''
    if num % 2 == 0 :
        answer = 'Even'
    else :
        answer = 'Odd'
        
    return answer

## 다른사람 풀이
## 논리연산자를 이용한 방법이라고 한다.
# num % 2가 거짓(0)이라면 num % 2 ==0 (거짓) and Odd 가 되므로
# 둘 다 참이어야하는 조건에 맞지 않기 때문에 or Even으로 해서 둘 중에 하나라도 참일 때 가능한 Even이 출력되며
# num%2가 1(참)이면 and 조건이 성립되어 Odd가 출력됩니다

# 파이썬 A or B에서 A
def evenOrOdd(num):
    #함수를 완성하세요
    if num%2:
        return "Odd"

    return "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))