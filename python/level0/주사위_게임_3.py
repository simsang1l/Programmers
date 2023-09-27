def solution(a, b, c, d):
    answer = 0
    dct = { 1: []
          , 2: []
          , 3: []
          , 4: []}
    lst = sorted([a, b, c, d], reverse = True)
    se = sorted(set(lst), reverse = True)
    for i in set(lst):
        cnt = 0
        for j in lst:
            if i == j :
                cnt += 1
        dct[cnt].append(i)
    
    if len(se) == 1:
        answer = 1111 * a
        
    elif len(se) == 2:
        if dct[3]:
            p = dct[3].pop()
            q = dct[1].pop()
            answer = (10 * p + q)**2
        else:
            p, q = dct[2]
            answer = (p + q) * abs(p - q)
    elif len(se) == 3 :
        p = dct[2]
        q, r = dct[1]
        answer = q * r
    elif len(se) == 4:
        answer = min(dct[1])
            
    
    return answer