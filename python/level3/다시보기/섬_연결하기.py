"""
다른사람 풀이
1. kruscal algorithm
    1. 비용을 오름차순 정렬
    2. 정렬된 간선 리스트에서 순서대로 조회하며 사이클을 형성하지 않는 간선 선택
    3. 해당 간선을 현재 MST(minimum spanning tree, 최소 비용 신장 트리) 집합에 추가

내가 이해한대로 해설
1. 비용을 오름차순 정렬
2. 연결된 노드가 있는 link라는 set생성
3. 연결된 노드가 있다면 넘어가고 없다면 연결된 노드라는 표시로 link에 값 추가
4. 비용이 오름차순으로 정렬되어 있으므로 비용만 더하면 끝!
"""
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    link = set([costs[0][0]])
    
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break
    
    return answer