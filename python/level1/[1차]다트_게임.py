import re 

def solution(dartResult):
    answer = 0
    # S: **1, D: **2, T: **3
    # *: result*2 + (result-1) * 2, 1번째의 경우 result*2, 중첩가능(#이라면 -2*result)
    # #: -result 
    
    # [point1, point2, point3]
    point = re.findall('[0-9]+', dartResult)
    point = list(map(int, point))
    cal = re.sub('[0-9]+', '0', dartResult)
    idx = -1

    for i in cal:
        if i.isdigit():
            idx += 1
        else :
            if i == 'S':
                point[idx] = point[idx]**1
            elif i == 'D':
                point[idx] = point[idx]**2
            elif i == 'T':
                point[idx] = point[idx]**3
            elif i == '*':
                if idx == 0:
                    point[idx] = point[idx] * 2
                else :
                    point[idx] = point[idx] * 2
                    point[idx-1] = point[idx-1] * 2
            elif i == '#':
                point[idx] = point[idx] * (-1)

    answer = sum(point)
    
    return answer

## 다른 사람 풀이 
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace("10", "A") # 계산하기 편하게 하기 위해 10을 A로 변환
    sdt = ['S', 'D', 'T'] # S: 1제곱, D: 2제곱, T: 3제곱

    # 초기 시작 값이 "A"라면 10으로 시작
    if dartResult[0] == "A":
        cnt = 10

    # 그게 아니라면 수로 시작
    else:
        cnt = int(dartResult[0])

    # 반복문을 통해 문자를 확인
    for i in dartResult[1:]:

        # 문자가 sdt에 포함되어 있다면
        if i in sdt:
            cnt = cnt ** (sdt.index(i) + 1) # 현재 수에서 sdt의 인덱스+1 제곱을 한다.

        # 문자가 "*"이라면 현재 수를 두배해주고 이전에 수가 있다면 이전 수도 두배해준다.
        elif i == "*":
            cnt *= 2
            if answer:
                answer[-1] *= 2

        # 문자가 "#"라면 현재 수를 - 해준다.
        elif i == "#":
            cnt = -cnt

        # 그 외 문자라면 숫자인 것으로 게임 한판이 끝난 것이다.
        else:
            answer.append(cnt) # 점수를 answer 추가

            # 다음 게임의 시작 값으로 초기화
            if i == "A":
                i = 10
            cnt = int(i)

    # 마지막 게임 점수 추가
    answer.append(cnt)

    return sum(answer)