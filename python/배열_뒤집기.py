def solution(num_list):
    answer = []
    # num_list를 역순으로 읽어 새로운 리스트에 담는다.
    for i in range(len(num_list) - 1, -1, -1):
        answer.append(num_list[i])
    
    return answer