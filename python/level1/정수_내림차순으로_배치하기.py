def solution(n):
    # sorted하니 알아서 list로 변환됐다 ...
    answer = int(''.join(sorted(str(n), reverse = True)))
    return answer

## 다른사람 풀이
