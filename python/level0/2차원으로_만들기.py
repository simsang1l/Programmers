# 리스트에서 n개만큼 인덱스 접근
# 빈 리스트에 append
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])

    return answer