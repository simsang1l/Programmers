def solution(s):
    answer = 0
    num = {'zero': 0,
           'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}
    
    for i, n in num.items() :
        s = s.replace(i, str(n))
    answer = int(s)
        
    return answer

# 다른 사람 풀이
## range로 하는게 이 문제에선 더 빠르긴 하다..
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, val in enumerate(words):
        s = s.replace(words[i], str(i))

    return int(s)