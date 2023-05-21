def solution(n,a,b):
    answer = 0
    # [1, 2], [3, 4]... 이런 대진이다.
    # 몫이 같으면 같은 그룹에 있다
    # 홀수의 경우 2로 나누면 몫이 1 작으므로 1을 더해줘 같은 그룹임을 알게 한다.
    # 이긴 그룹의 경우 번호가 다시 부여되는 형식임
    # 이기면 1판 하는 것
    while a != b:
        answer += 1

        a, b = (a + 1)//2, (b + 1)//2

    return answer

# 다른 사람 풀이
## 이해가 되지 않아~, xor를 이용하는 거라고 합니다아아...
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()