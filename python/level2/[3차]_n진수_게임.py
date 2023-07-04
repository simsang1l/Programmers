def make_n_num(n, q):
    rev_base = ''
    dic = {  10: 'A'
           , 11: 'B'
           , 12: 'C'
           , 13: 'D'
           , 14: 'E'
           , 15: 'F'
          }
    while n > 0 :
        n, mod = divmod(n, q)
        if mod in (10, 11, 12 ,13 ,14 ,15):
            mod = dic[mod]
        rev_base += str(mod)
        
    return rev_base[::-1]
        
    
def solution(n, t, m, p):
    answer = ''
    cnt = 1 # 1부터 늘려가며 말할 숫자 만들기용
    lst = ['0'] # 말할 숫자가 모두 적혀 있는 리스트
    
    while m * t >= len(lst):
        num = make_n_num(cnt, n)

        for i in num:
            lst.append(i)
            
        cnt += 1
        
    for idx, value in enumerate(lst[:t*m]) :
        if (idx) % m == p-1 :
            answer += value
        
    return answer