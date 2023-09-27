def solution(number):
    answer = 0
    a = int(number) % 9
    b = sum([int(i) for i in number]) % 9

    answer = a
    return answer

# 다른 사람 풀이
## map 이용하기
def solution(number):
    return sum(list(map(int, number))) % 9