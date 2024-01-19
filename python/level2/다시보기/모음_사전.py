# 나올 수 있는 경우의 수 구하기
# 정렬하기(A, E, I, O, U, AA 이런식으로 나오던 문자를 A, AA, AAA, AAAA, AAAAA 이렇게 나오도록!)
# 해당 값의 index + 1을 구하면 몇 번째인지 알 수 있음
from itertools import product

def solution(word):
    answer = []
    alpha = ['A', 'E', 'I', 'O', 'U'] 
    
    for i in range(1, 6) :
        for j in list(product(alpha, repeat = i)):
            answer.append(''.join(j))
    answer.sort()
    answer = answer.index(word) + 1
            
    
    return answer
    
solution("AAAAE")


# chatgpt의 답변
def solution_recursive(word):
    # 사전에서 각 문자가 나타나는 순서
    order = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    # 사전에서 각 자리가 가지는 가중치
    # 예: 첫 번째 자리가 바뀌면 5^4개의 단어가 새로 시작
    weights = [781, 156, 31, 6, 1]

    # 재귀 함수 정의
    def calculate_position(word, depth):
        if not word:
            return 0
        # 첫 글자에 대한 위치 계산 및 재귀 호출
        first_char = word[0]
        return order[first_char] * weights[depth] + calculate_position(word[1:], depth + 1)

    # 재귀 함수 호출
    return calculate_position(word, 0) + len(word)  # 단어의 길이를 더해 최종 순서 계산