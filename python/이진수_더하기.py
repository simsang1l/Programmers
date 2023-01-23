def solution(bin1, bin2):
    answer = ''
    # 2진수를 10진수로 변경하기 int(val, 2)
    val1 = int(bin1, 2)
    val2 = int(bin2, 2)
    # 10진수를 2진수로 변경하기 bin()
    ## oct() : 8진수로
    ## hex() : 16진수로
    result = bin(val1 + val2)
    answer = result[2:]
    
    return answer