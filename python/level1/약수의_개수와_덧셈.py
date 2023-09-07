def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        leftover = 0
        for i in range(1, num+1):
            if num % i == 0:
                leftover += 1
        if leftover % 2 == 0 :
            answer += num
        else : 
            answer -= num
            
    return answer

# 다른 사람 풀이 
## 제곱수의 약수는 홀수개임을 이용
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        # ex) 5를 제곱근으로 가지는 25의 약수는 1, 5 25 3개임
        # 반면 10의 제곱근은 3.1622... 으로 정수가 아닌데 10의 약수는 1, 2, 5, 10 4개
        # int(i**0.5)를 사용하면 정수로 바뀌니 두 값이 같으면 제곱수가 되므로 약수의 개수는 홀수
        if int(i**0.5)==i**0.5: 
            answer -= i
        else:
            answer += i
    return answer

