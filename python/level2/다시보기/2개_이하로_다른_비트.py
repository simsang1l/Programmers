"""
주어진 수에서 1부터 키워 나가며 XOR적용
테스트 10, 11에 시간초과 발생
"""
def solution(numbers):
    answer = []
    
    # 비트가 다른 수가 필요하므로 XOR이용!
    for num in numbers:
        cnt = 3
        c_num = num
        while cnt > 2 :
            # 비교할 숫자
            c_num += 1
            result = bin(num ^ c_num)

            cnt = sum(list(map(int, result[2:])))

        answer.append(c_num)
                
    return answer

# 다른 사람 풀이
"""
1. 주어진 숫자가 짝수인 경우 가장 마지막(오른쪽) 비트가 0이다.
   마지막 비트를 0에서 1로 바꿔준 값이 답임.
   --> 비트가 1 ~ 2개 다른 수들 중에서 제일 작은수 이기 때문
2. 주어진 숫자가 홀수인 경우.
   가장 오른쪽에 있는 0을 1로 바꿔주고 그 다음 비트를 0으로 바꿔준다.
   - 비트를 1번만 바꾸기 위해 짝수처럼 적용한다면 7(0111) 같은 숫자는 8(1000)이 되기 때문에 불가
   - 그렇다면 2번 바꾸는 방법을 선택할 수 있음.
     가장 작은 수를 구해야 하기 때문에 가장 마지막에 나오는 0을 1로 그 다음 수를 0으로 바꿔줌
"""
def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
            continue
            
        number_bin = '0' + bin(num)[2:]
        number_bin = number_bin[:number_bin.rindex('0')] + "10" + number_bin[number_bin.rindex("0") + 2:]
        answer.append(int(number_bin, 2))
        
    return answer