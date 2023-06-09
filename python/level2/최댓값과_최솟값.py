def solution(s):
    answer = ''
    ss = s.split(' ')
    # map 함수를 이용하여 형 변환(음수인데 문자열인 경우 min, max값이 반대로 나옴)
    ss = list(map(int, ss))
    
    answer += (str(min(ss)) + ' '+ str(max(ss)))
    
    return answer