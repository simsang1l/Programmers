def solution(survey, choices):
    answer = ''
    score = {
            '1': 3,
            '2': 2,
            '3': 1,
            '4': 0,
            '5': 1,
            '6': 2,
            '7': 3,
        }
    
    p_type = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }
    
    for sv, ch in zip(survey, choices):
        if ch < 4 :
            p_type[sv[0]] += score[str(ch)]
        elif ch > 4:
            p_type[sv[1]] += score[str(ch)]
    
    # 여기서 어떻게 해야할지 길을 잃었다 ...
    if p_type['R'] >= p_type['T']:
        answer+='R'
    else :
        answer+='T'
        
    if p_type['C'] >= p_type['F']:
        answer+='C'
    else :
        answer+='F'
        
    if p_type['J'] >= p_type['M']:
        answer+='J'
    else :
        answer+='M'
        
    if p_type['A'] >= p_type['N']:
        answer+='A'
    else :
        answer+='N'
    
    return answer

# 다른 사람 풀이
def solution(survey, choices):
    
    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            # "TR"과 같이 거꾸로 들어오는 경우 "RT"로 변경
            # "R", "C", "J", "M"에 대해서는 양수 덧셈, 반대는 음수 덧셈
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result