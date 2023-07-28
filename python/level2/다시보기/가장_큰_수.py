# 문자열이 0이상 1000이하라는 점을 이용하여 3자리수까지 비교하는 방법 이용!
def solution(numbers):    
    s = list(map(str,numbers))
    a = sorted(s,key=lambda x: x*3,reverse=True)
    
    return str(int("".join(a))) # [0, 0] 이런 경우 00으로 출력되기 때문에 int()를 붙여줌