def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        
        if mode == 0:
            if code[idx] != '1' and idx % 2 == 0:
                answer += code[idx]
            elif code[idx] == '1' :
                mode = 1
        elif mode == 1 :
            if code[idx] != '1' and idx % 2 != 0 :
                answer += code[idx]
            elif code[idx] == '1':
                mode = 0
    if answer == '':
        answer = 'EMPTY'
        
    return answer

# 다른 사람 풀이 
# 1을 기준으로 mode가 바뀌고
# index가 홀수인지 짝수인지를 기준으로 판별해서 이렇게 작성한 것 같음
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"