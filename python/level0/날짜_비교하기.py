def solution(date1, date2):
    answer = 0
    # year로 비교
    if date1[0] > date2[0] : 
        answer = 0
    elif date1[0] < date2[0] : 
        answer = 1
    # year가 같은 경우
    else :
        # month로 비교
        if date1[1] > date2[1]:
            answer = 0
        elif date1[1] < date2[1]:
            answer = 1
        else :
            if date1[2] > date2[2]:
                answer = 0
            elif date1[2] < date2[2]:
                answer = 1
            # 년, 월, 일 모두 같은 경우
            else :
                answer = 0
    return answer
    
# 다른 사람 풀이
# 리스트간의 비교도 가능하네..?
def solution(date1, date2):
    return int(date1 < date2)

# 내 풀이에서 이런게 필요했다..
def solution(date1, date2):
    for i in range(3):
        if date1[i]<date2[i]:return 1
        elif date2[i]<date1[i]: return 0
    return 0