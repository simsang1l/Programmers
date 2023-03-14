def solution(numbers, hand):
    answer = ''
    # 왼손, 오른손의 현재 위치 기록 필요
    keypad = { 1: [0, 0], 2:[0, 1], 3: [0,2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    left = keypad['*']
    right = keypad['#']
    
    for num in numbers:
        now = keypad[num]
        
        if num in [1, 4, 7]:
            answer += 'L'
            left = now 
        elif num in [3, 6, 9]:
            answer += 'R'
            right = now
        else:
            left_now = 0
            right_now = 0
            # 좌표 거리 계산
            for a, b, c in zip(left, right, now):
                left_now += abs(a - c)
                right_now += abs(b - c)
            # 왼손이 더 가까운 경우
            if left_now < right_now :
                answer += 'L'
                left = now
            # 오른손이 더 가까운 경우
            elif right_now < left_now :
                answer += 'R'
                right = now
            # 두 거리가 같은 경우
            else :
                if hand == 'left':
                    answer += 'L'
                    left = now
                else:
                    answer += 'R'
                    right = now
            
    return answer