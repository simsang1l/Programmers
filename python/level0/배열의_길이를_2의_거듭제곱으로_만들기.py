def solution(arr):
    answer = []
    arr_len = len(arr)
    length = []
    for i in range(11):
        length.append(2**i)
    
    for i in range(len(length)-1):
        if arr_len == length[i] :
            answer = arr
            break
        elif arr_len > length[i] and arr_len < length[i+1]:
            answer = arr + ([0]*(length[i+1] - arr_len))
            break

    return answer

# 다른 사람 풀이
# a에 2의 거듭제곱을 하며 비교를 하는 방법, 굳이 거듭제곱한걸 저장할 필요가 없었다.
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)