# 테스트 12, 13, 효율성테스트 시간초과
# n-factorial만큼 경우의 수가 생기므로 
# 전체 경우의 수를 만들고 나서 k번째를 찾기보단 k번째만 빠르게 찾는 방법이 필요함
from itertools import permutations

def solution(n, k):
    answer = []
    lst = [x for x in range(1, n+1)]
    
    permute = permutations(lst, n)
    order = [x for x in list(permute)]
    answer = order[k-1]
    
    return answer

# 수정 코드
# 주어진 문제에서 앞자리가 1이 되는 경우는 2개 (n=3인 경우 2개 숫자만 번갈아 가면서 정렬하기 때문에 2! = 2)
# 이 점을 이용해서 맨 처음 수는 (k-1) // (n-1)! (인덱스 접근을 해야하기 때문에 k-1을 사용해야함)
# 처음 수가 결정되면, 다음에 올 숫자를 구하기 위해 k % (n-1)!
# n을 1씩 감소 시켜 그 다음에 오는 원소를 구한다

import math

def solution(n, k):
    answer = []
    lst = [i for i in range(1, n + 1)]

    while lst:
        # 몇 번째 앞자리 숫자리의 그룹에 있는지 구분
        a = (k - 1) // math.factorial(n - 1)
        answer.append(lst.pop(a))

        # 그룹내에 몇 번째 위치에 있는지 구분
        k = k % math.factorial(n - 1)
        n -= 1

    return answer