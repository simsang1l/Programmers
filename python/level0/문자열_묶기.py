def solution(strArr):
    answer = 0
    dic = {}
    for i in strArr:
        if len(i) not in dic :
            dic[len(i)] = [i]
        else:
            dic[len(i)].append(i)
            
    dic = sorted(dic.items(), key = lambda x: len(x[1]), reverse = True)
    
    answer = len(dic[0][1])
    
    return answer

# 다른 사람 풀이
# len인 index에 값을 1씩 더하는 방식으로 개수를 저장하는 방법
def solution(strArr):
    a=[0]*31
    for x in strArr:
        a[len(x)]+=1

    return max(a)