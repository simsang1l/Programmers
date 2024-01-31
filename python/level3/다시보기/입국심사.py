"""
이진 탐색에 대해 다른 글들을 조금더 봐보자
"""

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
            mid = (left+ right) // 2
            people = 0
            for time in times:
                # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
                people += mid // time
                # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
                if people >= n:
                    break
            print(left, right, mid, people)
            # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
            if people >= n:
                answer = mid
                right = mid - 1
            # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
            elif people < n:
                left = mid + 1

    return answer