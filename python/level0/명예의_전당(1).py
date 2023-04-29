def solution(k, score):
    answer = []
    queue = []
    
    for i in score :
        if len(queue) == k and i > min(queue):
            queue.append(i)
            queue.sort()
            queue.pop(0)
            answer.append(min(queue))
        elif len(queue) == k and i <= min(queue) :
            answer.append(min(queue))
        else :
            queue.append(i)
            queue.sort()
            answer.append(min(queue))
        
    return answer

# 다른 사람 풀이
## 새 점수가 명예의 전당에 있는 최소값보다 크다면 그 최소값을 밀어내는 구조
def solution(k, score):
    
    q = []
    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer