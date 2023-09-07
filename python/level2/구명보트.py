# greedy!
# 1. 큰것부터 처리하자! 로 접근하면 해결방법이 보인다.

# 현재까지의 합이 limit보다 크거나 같으면 endpointer가 가리키고 있는 값의 index를 1 줄인다
# startpointer와 endpointer가 같거나 교차되면 종료
# 현재까지 합이 limit보다 작은 경우 startpointer를 1 증가 endpointer의 값의 index를 1 줄인다

def solution(people, limit):
    answer = 0

    people = sorted(people)
    startpointer = 0
    endpointer = len(people)-1

    while startpointer <= endpointer:
        if people[startpointer] + people[endpointer] > limit:
            answer += 1
            endpointer -= 1
        else:
            answer += 1
            endpointer -= 1
            startpointer += 1

    return answer


# 다른 사람 풀이 
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer