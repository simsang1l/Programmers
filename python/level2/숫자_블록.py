# 소수면 1 아니면 약수중 가장 큰 수 이렇게 구하려고 했지만 테스트13번과 효율성 테스트에서 실패
# 어떤수의 제곱근까지 확인하면 약수를 알 수 있음.(n x m 형태에서 n을 구할 수 있으니 가장 큰 m을 구할 수 있겠지요)
# 문제에서 천만 이상의 숫자가 적힌 블록은 나올 수 없음! --> 테스트 13번 해결

def solution(begin, end):
    answer = []
    
    for i in range(begin,  end + 1):
        min_val = 1
        max_val = 1
        
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                if i // j <= 10**7:
                    min_val = j
                    answer.append(i // j)
                    break
                else :
                    max_val = j
        if i == 1 :
            answer.append(0)
        elif min_val == 1:
            answer.append(max_val)
        
    return answer