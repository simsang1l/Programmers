def solution(my_string, queries):
    answer = ''
    lst = list(my_string)

    for s, e in queries:
        if s == 0 :
            lst[s:e+1] = lst[e::-1]
        else :
            lst[s:e+1] = lst[e:s-1:-1]
        
    
    answer = ''.join(lst)
    
    return answer

# 다른 사람 풀이
## 조회한 문자열을 뒤집는 방법이..!
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)