def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base 

def solution(n):
    answer = 0
    
    num = convert(n, 3)
    answer = int(str(num), 3)
    
    return answer