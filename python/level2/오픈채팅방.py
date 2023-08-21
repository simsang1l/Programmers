def solution(record):
    answer = []
    # 딕셔너리 생성 {uid: 채팅방에서의 이름}
    # 최종 채팅방에서의 이름을 만든다
    # result의 이름을 변경하여 출력!
    name = {}
    for i in record:
        extraction = i.split(' ')
        
        if 'Enter' in i:
            name[extraction[1]] = extraction[2]
        elif 'Change' in i:
            name[extraction[1]] = extraction[2]
    
    for i in record :
        extraction = i.split(' ')
        if 'Enter' in i:
            answer.append(f"{name[extraction[1]]}님이 들어왔습니다.")
        elif 'Leave' in i:
            answer.append(f"{name[extraction[1]]}님이 나갔습니다.")
            
            
    return answer