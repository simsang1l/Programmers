def solution(babbling):
    answer = 0
    ong = ['aya', 'ye', 'woo', 'ma']
    for i in babbling :
        for o in ong:
            if o * 2 not in i :
                # 텍스트를 빈값으로 바꿨을때 연결되어 발음되는 말이라면 안되므로
                # 1칸 공백으로 변경
                i = i.replace(o, ' ')
        if i.strip() == '' :
            answer += 1
        
            
    return answer