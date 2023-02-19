def solution(s):
    answer = ''
    word = s.split(' ')
    
    for i, wrd in enumerate(word):
        # 단어별 인덱스 파악
        for idx, value in enumerate(wrd):
            # 인덱스가 짝수인 경우 대문자, 홀수인 경우 소문자 변환
            if idx % 2 == 0:
                value = value.upper()
            else :
                value = value.lower()
            
            answer += value
        # 마지막 단어 다음엔 공백을 추가하지 않는다  
        if i+1 != len(word):
            answer += ' '
            
    return answer

# 다른사람 풀이
## list 이용해서 푸는 사람이 많은 것 같다..
def solution(s):
    answer = []
    s = s.split(' ')

    for i in range(len(s)):
        result = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        answer.append(result)

    return ' '.join(answer)