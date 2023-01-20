# 남의 solution이지만... 가장 이해하기 쉬운 코드 같음

def solution(babbling):
    c = 0
    for b in babbling:
        print('bb;', b)
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
                print(b)
        if len(b.strip()) == 0:
            c += 1
    return c