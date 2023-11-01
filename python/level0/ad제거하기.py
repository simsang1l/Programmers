def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' in i :
            continue
        else :
            answer.append(i)
            
    return answer

# 다른 사람 풀이
# 리스트 컴프리헨션 사용법 복기
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]