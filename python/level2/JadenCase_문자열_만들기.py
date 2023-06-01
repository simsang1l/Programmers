# 문자열내에 공백이 있는경우를 생각해줘야함
# 맨 앞에 공백이 있을경우?
def solution(s):
    answer = ''
    lst = []
    s = s.split(' ')
    for i in s :
        if i:
            lst.append(i[0].upper() + i[1:].lower())
        else :
            lst.append(i)
    
    answer = ' '.join(lst)
    
    return answer