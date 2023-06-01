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

# 다른 사람 풀이
## capitalize라는 함수가 구현되어 있기도 하다
def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer