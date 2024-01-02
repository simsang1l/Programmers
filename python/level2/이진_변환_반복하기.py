def solution(s):
    answer = []
    val = s
    cnt_0 = 0
    cnt = 0 # 회차
    
    while val != '1' :
        cnt_0 += sum([1 for i in val if i == '0' ])
        cnt += 1 
        val = val.replace('0', '')
        length = len(val)
        
        val = bin(length)[2:]
    
    answer = [cnt, cnt_0]
    
    return answer