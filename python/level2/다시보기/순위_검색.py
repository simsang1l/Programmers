def solution(info, query):
    # 점수를 제외한 나올 수 있는 모든 조건
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    # 지원자 정보에 해당하는 점수 넣기
    for i in info:
            i = i.split()
            for a in [i[0], '-']:
                for b in [i[1], '-']:
                    for c in [i[2], '-']:
                        for d in [i[3], '-']:
                            data[(a, b, c, d)].append(int(i[4])) 

    # 지원자 점수 오름차순 정렬
    for k in data:
        data[k].sort()
    
    # 원하는 조건에 맞는 인원 수
    answer = list()

    for q in query:
        q = q.split()
        # 개발자의 정보에 해당하는 사람의 점수
        scores = data[(q[0], q[2], q[4], q[6])]

        # query에서 필요한 점수
        wanted = int(q[7])

        # 이진탐색을 위한 index정보, l은 탐색 범위의 시작인덱스 r은 탐색 범위의 종료 인덱스
        l, r = 0, len(scores)
        
        while l < r:
            middle = (l + r)//2
            # 지원자의 점수가 원하는 조건보다 클 경우 종료 범위를 middle의 index로 대체
            if scores[middle] >= wanted:
                r = middle
            # 지원자 점수가 원하는 조건보다 작으니 middle index에 있는 값보단 큰 경우를 나타냄.(middle index 이후에 해당 값이 있을것임)
            # 따라서 l의 index 증가
            else :
                l = middle + 1
        # while문에서 최소 탐색 index를 찾았으니 그 index이후에 있는 값들은 조건에 해당하는 값
        answer.append(len(scores) - l)

    return answer

# 효율성 테스트만 실패...
def solution(info, query):
    answer = []
    for q in query:
        s = q.replace('and ', '').split(' ') # query의 항목
        cnt = 0
        
        for i in info :
            state = 0
            t = i.split(' ') # info의 항목

            for idx in range(len(t)) :
                
                if s[idx] == '-' or t[idx] == '-':
                    state = 1
                elif s[idx] == t[idx]:
                    state = 1
                elif idx == 4 and int(t[idx]) >= int(s[idx]):
                    state = 1
                else :
                    state = 0
                    break

            if state == 1:
                cnt += 1
        
        answer.append(cnt)
        
    return answer