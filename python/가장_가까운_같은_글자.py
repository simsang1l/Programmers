def solution(s):
    answer = []
    
    # 문자, index를 저장
    # index는 이전에 나타난 문자의 index가 저장되어 있음
    word_dic = {}
    
    for idx, word in enumerate(list(s)):
        if word not in word_dic:
            answer.append(-1)
            word_dic[word] = idx
        else:
            answer.append(idx - word_dic[word])
            word_dic[word] = idx
            
    return answer