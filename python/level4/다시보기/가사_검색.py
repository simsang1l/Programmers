# 다른사람 풀이
# trie(트라이)라는 자료구조를 이용하여 풀이!

"""
1. 글자수가 같은 것만 비교하기
2. 글자가 같은지 비교하기

정확성 테스트 통과

효율성 테스트
성공: 4, 5
실패: 1, 2, 3
"""
def solution(words, queries):
    answer = []
    words_dic = {}
    for i in words:
        if len(i) not in words_dic :
            words_dic[len(i)] = [i]
        else :
            words_dic[len(i)].append(i)
            
    for i in queries:
        if len(i) in words_dic:
            cnt = 0
            flag = 0
            for j in words_dic[len(i)]:
                for idx in range(len(i)):
                    if i[idx] == "?" or i[idx] == j[idx]:
                        flag = 1
                        continue
                    else :
                        flag = 0
                        break
                if flag == 1 :
                    cnt += 1
                
            answer.append(cnt)
        else :
            answer.append(0)
    
    return answer