def solution(polynomial):
    answer = ''
    # 3x -> xxx
    # 3x + x -> 4x -> xxxx
    # x의 개수
    # 숫자
    cnt_x, num = 0, 0
    
    for i in polynomial.split(" + "):
        # i[:-1] 항의 마지막 글자를 제외한 부분
        if i[-1] == 'x':
            cnt_x += int(t if (t := i[:-1]) else 1)
        else :
            num += int(i)
        
    result = []
    if cnt_x :
        result.append('x' if cnt_x == 1 else str(cnt_x) + 'x')
    if num :
        result.append(str(num))
        
    return ' + '.join(result)