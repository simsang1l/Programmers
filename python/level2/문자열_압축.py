def solution(s):
    lst = []
    length = len(s)
    answer = length
    
    for i in range(1, length) :
        start = 0 # idx 용도
        cnt = 1 # 같은 규칙 세는 용도
        result = '' #result 비우기

        if length % i == 0 :
            l = length // i
        else :
            l = length // i + 1
            
        for j in range(l):
            subset = s[start:start+i]
            if subset == s[start+i:start+i*2]:
                cnt += 1
            else :
                if cnt == 1 :
                    result += subset
                else :
                    result += (str(cnt) + subset)
                cnt = 1
                    
            start += i
                  
        if answer > len(result):
            answer = len(result)
             
    return answer
