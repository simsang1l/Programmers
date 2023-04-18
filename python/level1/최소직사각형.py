def solution(sizes):
    answer = 0
    size_y = []
    size_x = []
    
    for (x, y) in sizes:
        if x < y:
            size_x.append(y)
            size_y.append(x)
        else :
            size_x.append(x)
            size_y.append(y)
            
    answer = max(size_x) * max(size_y)
           
    return answer

# 다른 사람 풀이
## 각 항목별 최대값과 최소값을 추출 및 최소값에서도 최대값을 추출해 곱하기
## [x for x in sizes] --> 예시) [[60, 50], [30, 70], [60, 30]]
## [max(x) for x in sizes] --> 예시) [60, 70, 60]
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)