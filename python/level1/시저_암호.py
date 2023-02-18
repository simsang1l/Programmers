# 알파벳은 26개임
# ascii code 이용
# z 에서 1 더하면 a

def solution(s, n):
    answer = ''
    
    for i in s :
        if i == ' ':
            answer += ' '
        elif i.islower() == True:
            lpw = (ord(i) - ord('a') + n) % 26 + ord('a')
            answer += chr(lpw)
        elif i.isupper() == True:
            upw = (ord(i) - ord('A') + n) % 26 + ord('A')
            answer += chr(upw)
            
    return answer

## 다른사람 풀이
### 리스트로 만들고 값을 변경한다면 공백을 신경쓸필요 없을듯..
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+ n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+ n) % 26 + ord('a'))
    return "".join(s)