def solution(a, b):
    answer = ''
    # 1월 1일 --> 금요일
    # 윤년 --> 2월 29일
    
    # 1월 1일부터 요일 계산?
    
    day_of_the_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 월을 기준으로 직전 월까지 세기
    # idx 기준으로 요일 세기
    answer = day_of_the_week[(sum(days[:a-1]) + b - 1) % 7]
    
    
    return answer

# 다른 사람의 풀이
# datetime 라이브러리 이용

import datetime

def solution(a, b):
    date = 'MON TUE WED THU FRI SAT SUN'.split()
    print(datetime.datetime(2016, a, b))
    print(datetime.datetime(2016, a, b).weekday()) # 월요일일때 0을 반환하며,  (0, 1, 2, 3, 4, 5, 6) 중 한 값을 반환함
    return date[datetime.datetime(2016, a, b).weekday()]
    
    
    return answer