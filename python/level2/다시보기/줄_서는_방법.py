"""
테스트 12, 13과 효율성 테스트 실패
"""
from itertools import permutations
def solution(n, k):
    answer = []
    answer = list(permutations(range(1, n+1), n))[k-1]
    return answer

# 다른 사람 풀이
"""
n이 3일때 첫 번쨰 줄에 같은 숫자가 2개(n-1)!씩 반복되고
두번째 줄은 1개(n-2)!씩 반복되는걸 볼 수 있음. -> 규칙 확인

첫 번쨰로 출력되는 숫자는 k/(n-1)!번째에 있는 값임.
이후 첫 번째 값으로 출력된 값을 삭제하고 k%(n-1)!인 값으로 갱신해야함.
두 번째로 출력되는 숫자의 배열은 k/f(n-2)!에 있는 값.

나머지를 구하고 끝날 때까지 위 과정 반복!
"""

import math
def solution(n, k):
    answer = []
    lst = list(range(1, n+1))
    
    while n > 1:
        fac = math.factorial(n-1)
        num = lst[(k-1)//fac]
        answer.append(num)
        lst.remove(num)
        n -= 1
        k %= fac
        
    answer.append(lst[-1])
    
    return answer