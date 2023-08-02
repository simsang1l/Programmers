# 중앙에는 갈색이 올 수 없음을 이용 == 테두리쪽만 갈색이 올 수 있다
# 중앙에 노란색이 오기 위해선 가로나 세로의 길이가 3이상이어야함
# 3부터 시작하는 시작 값과 나눈 몫을 이용하여 brown, yellow가 몇 개 필요한지 알 수 있음
# 시작값 * 2 + (몫 - 2) * 2 = brown + yellow
# 가로 세로 크기를 순서로 return하며 가로의 길이는 세로의 길이와 같거나 길다.

def solution(brown, yellow):
    answer = []
    yellow_cnt = 0
    brown_cnt  = 0
    total_cnt = brown+yellow
    
    for i in range(3, total_cnt+1):
        if total_cnt % i == 0 :
            brown_cnt = (total_cnt // i - 2)*2 + i * 2
            yellow_cnt = total_cnt - brown_cnt
            print(brown_cnt, yellow_cnt)
            if brown == brown_cnt and yellow == yellow_cnt:
                answer.append(i)
                answer.append(total_cnt // i)
                break
    if answer[1] > answer[0] :
        answer[0], answer[1] = answer[1], answer[0]
    
    return answer