def solution(strings, n):
    answer = []
    # 단어 list index와 문자, n번째 글자를 가진 dictionary 이용
    ## {key: (문자, n번째 글자)}
    word = {}
    
    # index및 단어와 n번째 단어 dictionary에 담기
    for idx, value in enumerate(strings):
        word[idx] = (value, value[n])
    
    # dictionary 여러 값을 기준으로 정렬
    answer = [strings[key] for key, value in sorted(word.items(), key = lambda item: (item[1][1], item[1][0]) )]
    
    

    return answer


# 다른사람풀이
## 동일한 방법에 더 간단한 방법이 있었다
### lambda랑 친해지기 .....
def solution(strings, n):
    answer = sorted(strings, key=lambda x:(x[n],x))
    
    return answer
