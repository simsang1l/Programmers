# 초기 코드, 테스트 실패 항목 존재, 효율성 테스트 모두 시간초과
"""
원하는 방 번호를 하나씩 받아 dictionary에 해당 방 번호가 사용중인지 기록
"""
def solution(k, room_number):
    answer = []
    check = {}
    
    # 방 번호 현 상황 기록
    for i in range(1, len(room_number)+1):
        check[i] = False
    
    for i in range(len(room_number)):
        if room_number[i] not in answer and room_number[i] in check:
            answer.append(room_number[i])
            check[room_number[i]] = True
        elif room_number[i] not in answer and room_number[i] not in check:
            answer.append(room_number[i])
            check[room_number[i]] = True
        else :
            for key, val in check.items():
                if val == False :
                    answer.append(key)
                    check[key] = True

    return answer