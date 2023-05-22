def solution(n, words):
    answer = []
    
    # 중복된 단어 찾기
    # 틀린 글자로 시작하는 경우
    used_words = []
    
    for idx, word in enumerate(words):
        if idx == 0:
            used_words.append(word)
        
        elif word[0] != words[idx-1][-1] or word in used_words:
            answer.append(idx%n+ 1)
            answer.append(idx//n + 1)
            break 
            
        elif idx == len(words) - 1:
            answer = [0, 0]
            break
        else :
            used_words.append(word)
        
    return answer

# 다른 사람 풀이
## 굳이 used_words를 쓸 필요가 없었다 ... 
## if없이 그냥 else도 쓰네??
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]