def solution(array):
    answer = []
    # index, value를 가지는 array 생성 후 역순 정렬
    # 제일 처음 값 가져오기
    lst = []
    for idx, value in enumerate(array):
        lst.append([value, idx])
        
    
    lst.sort(reverse = True)
    answer = lst[0]
    
    return answer