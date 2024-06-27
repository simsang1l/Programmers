"""
1. 크기별 귤의 개수 구하기
2. 개수가 많은 크기부터 골라서 귤의 개수를 구하고
3. 귤이 더 많을 경우 담을 수 있을 만큼 담고 크기의 개수를 return하면 될듯
"""
def solution(k, tangerine):
    answer = 0
    size_count = {}
    
    # 크기별 귤의 개수 만들기
    for i in tangerine:
        if i not in size_count:
            size_count[i] = 1
        else :
            size_count[i] += 1
            
    # 귤 개수를 기준으로 내림차순 정렬
    size_count = sorted(size_count.items(), key = lambda x: x[1], reverse=True)
    
    tmp = 0
    for (size, cnt) in size_count:
        tmp += cnt
        answer += 1
        
        if tmp >= k :
            break
        
    
    return answer

# 다른 사람 풀이
## dictionary에서 key는 없어도 되고 value값만 있으면 된다
# Counter: key별로 개수를 나타내는 dictionary가 return됨
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer